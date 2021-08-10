package utils

import (
	"database/sql"
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCheckInList(t *testing.T) {
	list := []interface{}{sql.NullBool{}, sql.NullInt64{}}

	// not in list
	dst := reflect.TypeOf(sql.NullFloat64{})
	assert.Equal(t, false, CheckInList(dst, list))

	// in list
	dst = reflect.TypeOf(sql.NullInt64{})
	assert.Equal(t, true, CheckInList(dst, list))

	// nil list
	dst = reflect.TypeOf(sql.NullInt64{})
	assert.Equal(t, false, CheckInList(dst, nil))
}

type MyBase struct {
	BaseInt        int
	baseUnexported float64
}

type MyStruct struct {
	MyBase
	IntField        int
	unexportedField string
	NullBool        sql.NullBool
}

func TestGetFields(t *testing.T) {
	// nil
	assert.Equal(t, []string(nil), GetFields(nil, false, nil))

	// get Exported fields recursively
	assert.Equal(t, []string{"BaseInt", "IntField", "Bool", "Valid"}, GetFields(reflect.TypeOf(MyStruct{}), false, nil))

	// get all fields recursively
	assert.Equal(t, []string{"BaseInt", "baseUnexported", "IntField", "unexportedField", "Bool", "Valid"}, GetFields(reflect.TypeOf(MyStruct{}), true, nil))

	// get all fields recursively, exclude structs in dismissList
	assert.Equal(t, []string{"BaseInt", "baseUnexported", "IntField", "unexportedField", "NullBool"}, GetFields(reflect.TypeOf(MyStruct{}), true, []interface{}{sql.NullBool{}}))

}

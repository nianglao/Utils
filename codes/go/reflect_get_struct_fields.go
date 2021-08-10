package utils

import (
	"reflect"
)

// GetFields extract field name in a struct
// by default extracting Exported fields recursively, if need export all fields using includeUnexported = true
// if need dismiss some struct recursively such as sql.NullFloat64, use dismissList = []interface{}{sql.NullFLoat64{}}
func GetFields(t reflect.Type, includeUnexported bool, dismissList []interface{}) (fields []string) {
	if t == nil {
		return
	}
	for i := 0; i < t.NumField(); i++ {
		if t.Field(i).Type.Kind() == reflect.Struct && !CheckInList(t.Field(i).Type, dismissList) {
			fields = append(fields, GetFields(reflect.Indirect(reflect.New(t.Field(i).Type)).Type(), includeUnexported, dismissList)...)
		} else {
			if !includeUnexported && len(t.Field(i).PkgPath) > 0 {
				continue
			}
			fields = append(fields, t.Field(i).Name)
		}
	}
	return
}

func CheckInList(dst reflect.Type, list []interface{}) bool {
	for _, a := range list {
		if dst == reflect.TypeOf(a) {
			return true
		}
	}
	return false
}

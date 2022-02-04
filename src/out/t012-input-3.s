.data
TRUE:	.asciiz	"true"
FALSE:	.asciiz	"false"
NULL:	.asciiz	"null"

.text
	li $v0, 5
	syscall
	move $a0, $v0
	li $v0, 1
	syscall
	li $v0, 5
	syscall
	move $a0, $v0
	li $v0, 1
	syscall
	li $v0, 5
	syscall
	move $a0, $v0
	li $v0, 1
	syscall
	li $v0, 5
	syscall
	move $a0, $v0
	li $v0, 1
	syscall

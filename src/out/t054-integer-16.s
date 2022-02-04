.data
TRUE:	.asciiz	"true"
FALSE:	.asciiz	"false"
NULL:	.asciiz	"null"

.text
main:
	li $v0, 5
	syscall
	move $t0, $v0
	li $v0, 5
	syscall
	move $t1, $v0
	move $a0, $v0
	li $v0, 1
	syscall
	li $v0, 5
	syscall
	move $t0, $v0
	li $v0, 5
	syscall
	move $t1, $v0
	move $a0, $v0
	li $v0, 1
	syscall
	li $v0, 5
	syscall
	move $t0, $v0
	li $v0, 5
	syscall
	move $t1, $v0
	move $a0, $v0
	li $v0, 1
	syscall

	li $v0, 10
	syscall

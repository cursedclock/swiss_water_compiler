.data
TRUE:	.asciiz	"true"
FALSE:	.asciiz	"false"
NULL:	.asciiz	"null"

.text
	li $a0, 500
	li $v0, 9
	syscall
	move $a0, $v0
	li $a1, 500
	li $v0, 8
	syscall
	move $v0, $a0
	move $a0, $v0
	li $v0, 4
	syscall
	li $a0, 500
	li $v0, 9
	syscall
	move $a0, $v0
	li $a1, 500
	li $v0, 8
	syscall
	move $v0, $a0
	move $a0, $v0
	li $v0, 4
	syscall
	li $a0, 500
	li $v0, 9
	syscall
	move $a0, $v0
	li $a1, 500
	li $v0, 8
	syscall
	move $v0, $a0
	move $a0, $v0
	li $v0, 4
	syscall

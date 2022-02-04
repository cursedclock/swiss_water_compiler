.data
TRUE:	.asciiz	"true"
FALSE:	.asciiz	"false"
NULL:	.asciiz	"null"
L0:	.asciiz	"hello "
L1:	.asciiz	"world"

.text
	addi $sp, $sp, -4
	addi $sp, $sp, -4
	la $v0, L0
	sw $v0, 8($sp)
	la $v0, L1
	sw $v0, 4($sp)
	lw $v0, 8($sp)
	move $t0, $v0
	lw $v0, 4($sp)
	move $t1, $v0
	add $v0, $t0, $t1
	move $a0, $v0
	li $v0, 4
	syscall

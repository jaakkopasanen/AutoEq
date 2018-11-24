# Denon AHGC20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.8; 23 -9.0; 25 -9.1; 28 -9.3; 31 -9.3; 34 -9.3; 37 -9.2; 41 -9.1; 45 -9.0; 49 -8.9; 54 -8.7; 60 -8.4; 66 -8.2; 72 -7.9; 79 -7.5; 87 -7.1; 96 -6.7; 106 -6.3; 116 -5.9; 128 -5.4; 141 -4.8; 155 -4.3; 170 -3.7; 187 -3.1; 206 -2.4; 227 -1.9; 249 -1.6; 274 -1.5; 302 -1.7; 332 -2.0; 365 -2.7; 402 -3.6; 442 -4.4; 486 -4.3; 535 -3.0; 588 -1.6; 647 -0.7; 712 -0.2; 783 -0.2; 861 -0.5; 947 -0.6; 1042 0.7; 1146 2.8; 1261 4.8; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 2.9; 2973 2.8; 3270 6.0; 3597 2.1; 3957 -2.1; 4353 3.3; 4788 1.6; 5267 4.7; 5793 5.6; 6373 -0.2; 7010 1.9; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AHGC20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AHGC20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.29 | -9.5 dB |
| Peaking | 465 Hz  | 2.77 | -4.2 dB |
| Peaking | 1414 Hz | 3.22 | 4.4 dB  |
| Peaking | 2178 Hz | 1.46 | 5.9 dB  |
| Peaking | 5568 Hz | 5.99 | 5.6 dB  |
| Peaking | 942 Hz  | 3.84 | -2.7 dB |
| Peaking | 991 Hz  | 1.8  | 1.2 dB  |
| Peaking | 2863 Hz | 7.59 | -4.3 dB |
| Peaking | 3302 Hz | 3.61 | 4.9 dB  |
| Peaking | 3835 Hz | 9.4  | -6.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Denon%20AHGC20/Denon%20AHGC20.png)
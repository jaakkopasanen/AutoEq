# Denon AHGC20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 -8.8; 23 -9.0; 25 -9.1; 28 -9.3; 31 -9.3; 34 -9.3; 37 -9.2; 41 -9.1; 45 -9.0; 49 -8.9; 54 -8.7; 60 -8.4; 66 -8.2; 72 -7.9; 79 -7.5; 87 -7.1; 96 -6.7; 106 -6.3; 116 -5.9; 128 -5.4; 141 -4.8; 155 -4.3; 170 -3.7; 187 -3.1; 206 -2.4; 227 -1.9; 249 -1.6; 274 -1.5; 302 -1.7; 332 -2.0; 365 -2.7; 402 -3.6; 442 -4.4; 486 -4.3; 535 -3.0; 588 -1.6; 647 -0.7; 712 -0.2; 783 -0.2; 861 -0.5; 947 -0.6; 1042 0.7; 1146 2.8; 1261 4.8; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 2.6; 2973 2.3; 3270 6.1; 3597 1.1; 3957 -3.4; 4353 2.0; 4788 -0.2; 5267 2.2; 5793 3.1; 6373 -1.4; 7010 1.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AHGC20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AHGC20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 36 Hz    |  0.29 | -9.5 dB |
| Peaking | 465 Hz   |  2.79 | -4.2 dB |
| Peaking | 1414 Hz  |  3.15 | 4.5 dB  |
| Peaking | 2158 Hz  |  1.57 | 5.9 dB  |
| Peaking | 19725 Hz |  2.53 | -2.3 dB |
| Peaking | 249 Hz   |  3.92 | 0.9 dB  |
| Peaking | 931 Hz   |  6.91 | -1.6 dB |
| Peaking | 3329 Hz  | 11.17 | 5.1 dB  |
| Peaking | 3874 Hz  | 10.11 | -5.7 dB |
| Peaking | 5640 Hz  |  9.28 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Denon%20AHGC20/Denon%20AHGC20.png)
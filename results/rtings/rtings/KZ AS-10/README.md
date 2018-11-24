# KZ AS-10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.1; 28 -2.2; 31 -2.4; 34 -2.5; 37 -2.6; 41 -2.7; 45 -2.8; 49 -2.8; 54 -3.1; 60 -3.5; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.2; 96 -5.7; 106 -6.2; 116 -6.7; 128 -7.1; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.3; 206 -7.2; 227 -7.1; 249 -6.7; 274 -6.1; 302 -5.6; 332 -5.1; 365 -4.4; 402 -3.8; 442 -3.2; 486 -2.6; 535 -1.9; 588 -1.2; 647 -0.5; 712 0.1; 783 0.5; 861 0.7; 947 0.4; 1042 -0.4; 1146 -1.2; 1261 -2.2; 1387 -2.8; 1526 -3.5; 1678 -4.4; 1846 -5.3; 2031 -6.5; 2234 -7.4; 2457 -7.5; 2703 -6.2; 2973 -4.2; 3270 -3.4; 3597 -4.0; 3957 -5.6; 4353 -2.1; 4788 -2.9; 5267 -6.7; 5793 -4.2; 6373 -2.6; 7010 -0.7; 7711 0.3; 8482 0.0; 9330 -3.3; 10263 -4.6; 11289 -2.4; 12418 -2.1; 13660 -0.4; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ AS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ AS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 155 Hz   |  0.53 | -7.7 dB |
| Peaking | 2339 Hz  |  1.56 | -7.5 dB |
| Peaking | 5356 Hz  |  4.73 | -5.7 dB |
| Peaking | 10278 Hz |  4.12 | -4.7 dB |
| Peaking | 24000 Hz |  2.08 | -2.5 dB |
| Peaking | 27 Hz    |  1.33 | -1.5 dB |
| Peaking | 317 Hz   |  2.03 | -0.9 dB |
| Peaking | 808 Hz   |  2.45 | 2.5 dB  |
| Peaking | 3939 Hz  | 11.44 | -3.4 dB |
| Peaking | 7809 Hz  |  5.76 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/KZ%20AS-10/KZ%20AS-10.png)
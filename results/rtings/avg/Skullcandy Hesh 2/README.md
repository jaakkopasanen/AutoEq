# Skullcandy Hesh 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.6; 28 5.0; 31 4.5; 34 4.1; 37 3.9; 41 3.8; 45 3.6; 49 3.4; 54 3.0; 60 2.5; 66 2.1; 72 1.5; 79 1.0; 87 0.4; 96 -0.1; 106 -0.7; 116 -1.0; 128 -1.1; 141 -1.0; 155 -0.8; 170 -0.7; 187 -0.3; 206 0.8; 227 2.0; 249 3.2; 274 4.3; 302 5.5; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 5.9; 588 4.3; 647 2.0; 712 0.6; 783 0.2; 861 0.1; 947 0.1; 1042 -0.0; 1146 0.5; 1261 1.8; 1387 2.5; 1526 3.3; 1678 3.8; 1846 3.8; 2031 4.5; 2234 5.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.2; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.82 | 5.8 dB  |
| Peaking | 52 Hz   | 1.15 | 2.0 dB  |
| Peaking | 136 Hz  | 1.16 | -2.5 dB |
| Peaking | 374 Hz  | 1.28 | 7.0 dB  |
| Peaking | 3483 Hz | 0.75 | 6.8 dB  |
| Peaking | 545 Hz  | 4.23 | 3.2 dB  |
| Peaking | 903 Hz  | 1.04 | -2.7 dB |
| Peaking | 1663 Hz | 1.04 | 1.9 dB  |
| Peaking | 6008 Hz | 2.27 | 7.1 dB  |
| Peaking | 6491 Hz | 0.98 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)
# Sennheiser G4ME ONE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.6; 49 5.1; 54 4.6; 60 4.0; 66 3.3; 72 3.2; 79 3.6; 87 2.0; 96 0.9; 106 0.3; 116 -0.1; 128 -0.7; 141 -1.2; 155 -1.4; 170 -1.6; 187 -1.6; 206 -1.6; 227 -1.6; 249 -1.4; 274 -1.2; 302 -1.0; 332 -0.8; 365 -0.6; 402 -0.5; 442 -0.4; 486 -0.2; 535 -0.0; 588 0.3; 647 0.4; 712 0.4; 783 0.6; 861 0.5; 947 0.1; 1042 -0.0; 1146 0.2; 1261 0.8; 1387 2.1; 1526 3.3; 1678 4.1; 1846 4.1; 2031 3.3; 2234 2.1; 2457 1.2; 2703 1.0; 2973 1.9; 3270 3.4; 3597 4.9; 3957 5.9; 4353 4.7; 4788 0.7; 5267 -1.6; 5793 -0.4; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.2; 16529 -6.5; 18182 -8.6; 20000 -16.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser G4ME ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser G4ME ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.31 | 6.4 dB  |
| Peaking | 152 Hz  |  0.75 | -3.5 dB |
| Peaking | 1756 Hz |  2.51 | 4.4 dB  |
| Peaking | 3884 Hz |  4.1  | 6.2 dB  |
| Peaking | 6476 Hz |  9.27 | 5.2 dB  |
| Peaking | 989 Hz  |  1.33 | 1.4 dB  |
| Peaking | 1065 Hz |  2.5  | -2.0 dB |
| Peaking | 4289 Hz | 11.52 | 2.1 dB  |
| Peaking | 5533 Hz |  4.23 | -4.5 dB |
| Peaking | 6136 Hz |  5.33 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20G4ME%20ONE/Sennheiser%20G4ME%20ONE.png)
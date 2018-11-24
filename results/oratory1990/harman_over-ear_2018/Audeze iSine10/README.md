# Audeze iSine10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.8; 116 5.4; 128 5.1; 141 4.8; 155 4.6; 170 4.4; 187 4.2; 206 4.0; 227 3.9; 249 3.9; 274 3.9; 302 3.9; 332 4.0; 365 4.0; 402 3.9; 442 3.7; 486 3.4; 535 3.2; 588 2.9; 647 2.5; 712 2.0; 783 1.5; 861 0.9; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -0.9; 1387 -1.4; 1526 -0.6; 1678 1.9; 1846 5.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.19 | 6.2 dB  |
| Peaking | 436 Hz  | 1.03 | 2.3 dB  |
| Peaking | 1400 Hz | 1.53 | -7.0 dB |
| Peaking | 2133 Hz | 0.86 | 8.2 dB  |
| Peaking | 5152 Hz | 1.86 | 4.8 dB  |
| Peaking | 1020 Hz | 3.03 | -0.8 dB |
| Peaking | 1414 Hz | 1.75 | 1.3 dB  |
| Peaking | 1508 Hz | 5.18 | -1.7 dB |
| Peaking | 6451 Hz | 4.95 | 3.2 dB  |
| Peaking | 7640 Hz | 1.77 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20iSine10/Audeze%20iSine10.png)
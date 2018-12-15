# Koss ESP950

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.9; 128 5.4; 141 4.5; 155 3.7; 170 3.0; 187 2.6; 206 2.4; 227 2.2; 249 2.2; 274 2.3; 302 2.5; 332 2.8; 365 2.9; 402 3.0; 442 2.7; 486 2.5; 535 2.3; 588 2.2; 647 2.3; 712 2.3; 783 1.5; 861 0.5; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -0.2; 1526 1.4; 1678 2.9; 1846 5.8; 2031 6.0; 2234 6.0; 2457 5.7; 2703 3.7; 2973 2.7; 3270 3.4; 3597 5.1; 3957 5.9; 4353 5.8; 4788 6.0; 5267 5.8; 5793 3.9; 6373 4.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.3  | 6.0 dB  |
| Peaking | 109 Hz  | 1.32 | 2.8 dB  |
| Peaking | 431 Hz  | 1.26 | 2.5 dB  |
| Peaking | 2119 Hz | 2.86 | 6.0 dB  |
| Peaking | 4585 Hz | 1.56 | 6.3 dB  |
| Peaking | 702 Hz  | 5.12 | 1.4 dB  |
| Peaking | 1244 Hz | 2.41 | -1.9 dB |
| Peaking | 1807 Hz | 8.81 | 2.0 dB  |
| Peaking | 6633 Hz | 8    | 2.7 dB  |
| Peaking | 8020 Hz | 2.15 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Koss%20ESP950/Koss%20ESP950.png)
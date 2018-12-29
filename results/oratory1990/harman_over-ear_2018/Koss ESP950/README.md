# Koss ESP950

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.8; 79 3.8; 87 3.5; 96 3.4; 106 3.3; 116 3.6; 128 3.5; 141 3.1; 155 2.7; 170 2.4; 187 2.3; 206 2.3; 227 2.2; 249 2.2; 274 2.3; 302 2.5; 332 2.8; 365 2.9; 402 3.0; 442 2.7; 486 2.5; 535 2.3; 588 2.2; 647 2.3; 712 2.3; 783 1.5; 861 0.5; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -0.2; 1526 1.4; 1678 2.9; 1846 5.8; 2031 6.0; 2234 6.0; 2457 5.7; 2703 3.7; 2973 2.7; 3270 3.4; 3597 5.1; 3957 5.9; 4353 5.8; 4788 6.0; 5267 5.8; 5793 3.9; 6373 4.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.4  | 4.7 dB  |
| Peaking | 54 Hz   | 0.23 | 1.7 dB  |
| Peaking | 428 Hz  | 1.22 | 2.4 dB  |
| Peaking | 2119 Hz | 2.87 | 6.0 dB  |
| Peaking | 4584 Hz | 1.56 | 6.3 dB  |
| Peaking | 66 Hz   | 5.84 | 0.7 dB  |
| Peaking | 696 Hz  | 5.85 | 1.2 dB  |
| Peaking | 1230 Hz | 3.73 | -2.0 dB |
| Peaking | 6657 Hz | 7.94 | 2.7 dB  |
| Peaking | 8037 Hz | 2.21 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Koss%20ESP950/Koss%20ESP950.png)
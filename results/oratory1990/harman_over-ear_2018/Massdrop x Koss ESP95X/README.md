# Massdrop x Koss ESP95X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.9; 79 4.6; 87 4.5; 96 4.4; 106 4.2; 116 4.1; 128 3.8; 141 3.4; 155 2.9; 170 2.6; 187 2.4; 206 2.3; 227 2.3; 249 2.3; 274 2.5; 302 2.7; 332 2.9; 365 3.1; 402 2.9; 442 2.8; 486 2.6; 535 2.5; 588 2.4; 647 2.6; 712 2.6; 783 1.7; 861 0.7; 947 0.3; 1042 -0.2; 1146 0.0; 1261 0.7; 1387 2.1; 1526 3.4; 1678 3.9; 1846 4.2; 2031 5.4; 2234 5.8; 2457 5.2; 2703 4.7; 2973 3.8; 3270 3.4; 3597 4.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.9; 5793 4.1; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Koss ESP95X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Koss ESP95X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.3  | 6.3 dB  |
| Peaking | 121 Hz  | 2.07 | 0.3 dB  |
| Peaking | 433 Hz  | 1.07 | 2.5 dB  |
| Peaking | 2158 Hz | 1.84 | 5.1 dB  |
| Peaking | 4750 Hz | 1.59 | 6.1 dB  |
| Peaking | 708 Hz  | 4.21 | 1.5 dB  |
| Peaking | 1091 Hz | 1.85 | -1.7 dB |
| Peaking | 1512 Hz | 4.35 | 1.7 dB  |
| Peaking | 6514 Hz | 6.83 | 3.3 dB  |
| Peaking | 7778 Hz | 1.84 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Koss%20ESP95X/Massdrop%20x%20Koss%20ESP95X.png)
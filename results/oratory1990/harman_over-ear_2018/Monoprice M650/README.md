# Monoprice M650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -5.5; 23 -6.0; 25 -6.3; 28 -6.8; 31 -7.1; 34 -7.3; 37 -7.5; 41 -7.7; 45 -7.9; 49 -8.1; 54 -8.3; 60 -8.4; 66 -8.5; 72 -8.5; 79 -8.7; 87 -9.0; 96 -9.6; 106 -10.2; 116 -10.5; 128 -10.7; 141 -11.1; 155 -11.5; 170 -11.6; 187 -11.7; 206 -11.6; 227 -11.3; 249 -11.1; 274 -10.7; 302 -10.2; 332 -9.6; 365 -9.0; 402 -8.4; 442 -7.8; 486 -7.1; 535 -6.3; 588 -5.5; 647 -4.6; 712 -3.1; 783 -2.4; 861 -1.3; 947 -0.5; 1042 0.4; 1146 1.1; 1261 1.5; 1387 0.7; 1526 0.6; 1678 0.1; 1846 -1.0; 2031 -2.0; 2234 -2.8; 2457 -3.3; 2703 -3.9; 2973 -4.0; 3270 -1.7; 3597 0.5; 3957 3.6; 4353 2.5; 4788 1.4; 5267 -2.4; 5793 -5.0; 6373 -4.7; 7010 -4.7; 7711 -6.1; 8482 -3.9; 9330 -1.5; 10263 -2.4; 11289 -4.0; 12418 -2.4; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice M650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice M650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 54 Hz    | 0.27 | -7.3 dB |
| Peaking | 204 Hz   | 0.78 | -7.5 dB |
| Peaking | 430 Hz   | 1.5  | -4.1 dB |
| Peaking | 2662 Hz  | 4.45 | -4.2 dB |
| Peaking | 7453 Hz  | 2.13 | -6.0 dB |
| Peaking | 1223 Hz  | 2.95 | 2.7 dB  |
| Peaking | 3300 Hz  | 1.68 | -4.4 dB |
| Peaking | 4068 Hz  | 2    | 7.5 dB  |
| Peaking | 5708 Hz  | 5.53 | -4.4 dB |
| Peaking | 11559 Hz | 5.84 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Monoprice%20M650/Monoprice%20M650.png)
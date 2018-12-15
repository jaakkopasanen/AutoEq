# Monoprice M650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.4; 28 -0.8; 31 -1.1; 34 -1.4; 37 -1.6; 41 -2.0; 45 -2.3; 49 -2.7; 54 -3.0; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.6; 87 -5.3; 96 -6.3; 106 -7.4; 116 -8.1; 128 -8.8; 141 -9.7; 155 -10.5; 170 -11.0; 187 -11.4; 206 -11.5; 227 -11.3; 249 -11.1; 274 -10.7; 302 -10.2; 332 -9.6; 365 -9.0; 402 -8.4; 442 -7.8; 486 -7.1; 535 -6.3; 588 -5.5; 647 -4.6; 712 -3.1; 783 -2.4; 861 -1.3; 947 -0.5; 1042 0.4; 1146 1.1; 1261 1.5; 1387 0.7; 1526 0.6; 1678 0.1; 1846 -1.0; 2031 -2.0; 2234 -2.8; 2457 -3.3; 2703 -3.9; 2973 -4.0; 3270 -1.7; 3597 0.5; 3957 3.6; 4353 2.5; 4788 1.4; 5267 -2.4; 5793 -5.0; 6373 -4.7; 7010 -4.7; 7711 -6.1; 8482 -3.9; 9330 -1.5; 10263 -2.4; 11289 -4.0; 12418 -2.4; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice M650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice M650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 203 Hz   | 0.54 | -11.5 dB |
| Peaking | 519 Hz   | 0.93 | -4.5 dB  |
| Peaking | 2912 Hz  | 0.99 | -13.9 dB |
| Peaking | 4101 Hz  | 0.49 | 29.5 dB  |
| Peaking | 6091 Hz  | 0.48 | -22.3 dB |
| Peaking | 15 Hz    | 1.65 | 1.0 dB   |
| Peaking | 1222 Hz  | 6.57 | 0.9 dB   |
| Peaking | 9632 Hz  | 4.79 | 3.3 dB   |
| Peaking | 11730 Hz | 1.76 | -4.2 dB  |
| Peaking | 13355 Hz | 2.09 | 3.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Monoprice%20M650/Monoprice%20M650.png)
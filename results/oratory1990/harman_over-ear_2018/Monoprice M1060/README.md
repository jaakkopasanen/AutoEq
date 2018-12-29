# Monoprice M1060

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.5; 28 3.3; 31 3.1; 34 3.0; 37 2.9; 41 2.7; 45 2.5; 49 2.2; 54 1.9; 60 1.6; 66 1.3; 72 1.1; 79 0.9; 87 0.5; 96 0.2; 106 -0.2; 116 -0.5; 128 -0.9; 141 -1.2; 155 -1.5; 170 -1.7; 187 -1.8; 206 -1.9; 227 -1.9; 249 -1.7; 274 -1.2; 302 -0.5; 332 0.1; 365 0.4; 402 0.6; 442 0.5; 486 0.0; 535 -0.4; 588 -0.8; 647 -1.1; 712 -1.3; 783 -1.2; 861 -0.5; 947 0.0; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.2; 1526 -1.3; 1678 -1.9; 1846 -2.4; 2031 -2.1; 2234 -1.9; 2457 -1.8; 2703 -1.7; 2973 -1.7; 3270 -1.2; 3597 -0.5; 3957 -1.0; 4353 -2.2; 4788 -0.7; 5267 0.9; 5793 0.9; 6373 3.2; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.3; 12418 0.0; 13660 0.0; 15026 -1.3; 16529 -7.5; 18182 -14.0; 20000 -20.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice M1060 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice M1060 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.7  | 3.5 dB   |
| Peaking | 44 Hz    | 0.89 | 1.4 dB   |
| Peaking | 186 Hz   | 1.25 | -2.2 dB  |
| Peaking | 13983 Hz | 0.7  | 8.5 dB   |
| Peaking | 19532 Hz | 0.59 | -21.7 dB |
| Peaking | 396 Hz   | 3.45 | 1.2 dB   |
| Peaking | 688 Hz   | 3.96 | -1.2 dB  |
| Peaking | 2069 Hz  | 1.27 | -2.2 dB  |
| Peaking | 4280 Hz  | 9.25 | -2.2 dB  |
| Peaking | 6541 Hz  | 5.78 | 4.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Monoprice%20M1060/Monoprice%20M1060.png)
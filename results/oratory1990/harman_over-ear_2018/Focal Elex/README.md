# Focal Elex

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 4.4; 25 4.1; 28 4.0; 31 3.9; 34 3.8; 37 3.6; 41 3.3; 45 3.1; 49 2.9; 54 2.7; 60 2.4; 66 2.1; 72 1.8; 79 1.6; 87 1.2; 96 0.8; 106 0.5; 116 0.3; 128 0.1; 141 0.0; 155 -0.1; 170 -0.1; 187 -0.1; 206 -0.0; 227 0.1; 249 0.3; 274 0.6; 302 0.8; 332 1.1; 365 1.4; 402 1.5; 442 1.5; 486 1.6; 535 1.6; 588 1.7; 647 1.7; 712 1.4; 783 1.1; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.1; 1387 -0.8; 1526 -0.4; 1678 1.0; 1846 2.4; 2031 3.5; 2234 4.1; 2457 3.8; 2703 3.1; 2973 2.1; 3270 1.7; 3597 1.3; 3957 2.6; 4353 3.5; 4788 2.4; 5267 0.7; 5793 -1.0; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.0; 18182 -4.2; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 19 Hz    |  0.53 | 4.6 dB   |
| Peaking | 53 Hz    |  1.38 | 1.1 dB   |
| Peaking | 2321 Hz  |  2.56 | 4.3 dB   |
| Peaking | 4303 Hz  |  5.05 | 3.4 dB   |
| Peaking | 6647 Hz  |  9.01 | 4.2 dB   |
| Peaking | 558 Hz   |  1.12 | 1.9 dB   |
| Peaking | 1313 Hz  |  2.19 | -2.0 dB  |
| Peaking | 1881 Hz  |  4.97 | 1.1 dB   |
| Peaking | 5708 Hz  | 13.95 | -2.1 dB  |
| Peaking | 19846 Hz |  2.81 | -15.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elex/Focal%20Elex.png)
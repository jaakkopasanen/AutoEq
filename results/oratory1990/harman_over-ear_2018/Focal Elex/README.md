# Focal Elex

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.7; 87 5.0; 96 4.2; 106 3.4; 116 2.7; 128 2.0; 141 1.4; 155 0.9; 170 0.5; 187 0.2; 206 0.1; 227 0.1; 249 0.3; 274 0.6; 302 0.8; 332 1.1; 365 1.4; 402 1.5; 442 1.5; 486 1.6; 535 1.6; 588 1.7; 647 1.7; 712 1.4; 783 1.1; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.1; 1387 -0.8; 1526 -0.4; 1678 1.0; 1846 2.4; 2031 3.5; 2234 4.1; 2457 3.8; 2703 3.1; 2973 2.1; 3270 1.7; 3597 1.3; 3957 2.6; 4353 3.5; 4788 2.4; 5267 0.7; 5793 -1.0; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.0; 18182 -4.2; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.5  | 6.8 dB  |
| Peaking | 543 Hz  | 1.99 | 1.8 dB  |
| Peaking | 2325 Hz | 2.77 | 4.4 dB  |
| Peaking | 4292 Hz | 4.95 | 3.4 dB  |
| Peaking | 6663 Hz | 9.19 | 4.3 dB  |
| Peaking | 17 Hz   | 1.19 | 2.2 dB  |
| Peaking | 40 Hz   | 1.19 | -1.4 dB |
| Peaking | 77 Hz   | 2.25 | 1.5 dB  |
| Peaking | 182 Hz  | 2.1  | -1.3 dB |
| Peaking | 1296 Hz | 4.24 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elex/Focal%20Elex.png)
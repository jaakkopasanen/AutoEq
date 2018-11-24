# Audeze LCD-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.4; 31 4.7; 34 4.2; 37 3.7; 41 3.2; 45 3.0; 49 2.9; 54 2.8; 60 2.7; 66 2.5; 72 2.3; 79 2.1; 87 1.7; 96 1.3; 106 0.9; 116 0.5; 128 0.1; 141 -0.2; 155 -0.5; 170 -0.7; 187 -0.9; 206 -1.0; 227 -1.1; 249 -1.1; 274 -1.1; 302 -0.9; 332 -0.7; 365 -0.5; 402 -0.4; 442 -0.4; 486 -0.5; 535 -0.4; 588 -0.3; 647 -0.3; 712 -0.3; 783 -0.3; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.5; 1387 0.3; 1526 0.6; 1678 1.1; 1846 1.4; 2031 1.2; 2234 1.4; 2457 1.8; 2703 2.5; 2973 2.6; 3270 2.7; 3597 2.7; 3957 2.8; 4353 3.8; 4788 3.7; 5267 4.3; 5793 4.3; 6373 3.5; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.9; 13660 -2.8; 15026 -3.0; 16529 -6.0; 18182 -11.4; 20000 -19.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.9  | 5.9 dB   |
| Peaking | 71 Hz    | 0.92 | 1.9 dB   |
| Peaking | 212 Hz   | 0.71 | -1.4 dB  |
| Peaking | 3170 Hz  | 1.21 | 2.6 dB   |
| Peaking | 5547 Hz  | 2.67 | 4.0 dB   |
| Peaking | 806 Hz   | 4.19 | -0.3 dB  |
| Peaking | 1746 Hz  | 6.22 | 0.5 dB   |
| Peaking | 13025 Hz | 0.51 | 1.3 dB   |
| Peaking | 19798 Hz | 0.98 | -18.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-X/Audeze%20LCD-X.png)
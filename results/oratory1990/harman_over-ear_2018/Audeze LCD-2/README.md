# Audeze LCD-2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.8; 25 4.8; 28 4.7; 31 4.6; 34 4.5; 37 4.3; 41 4.1; 45 3.8; 49 3.6; 54 3.4; 60 3.3; 66 3.1; 72 2.9; 79 2.6; 87 2.3; 96 1.9; 106 1.5; 116 1.2; 128 0.8; 141 0.5; 155 0.2; 170 0.0; 187 -0.2; 206 -0.3; 227 -0.4; 249 -0.5; 274 -0.3; 302 -0.2; 332 0.1; 365 0.5; 402 0.6; 442 0.3; 486 0.0; 535 -0.1; 588 -0.3; 647 -0.2; 712 0.0; 783 0.5; 861 -0.0; 947 -0.1; 1042 0.1; 1146 0.9; 1261 1.7; 1387 1.2; 1526 1.0; 1678 2.5; 1846 3.3; 2031 3.9; 2234 4.0; 2457 2.4; 2703 2.3; 2973 2.5; 3270 4.0; 3597 5.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 3.1; 5793 1.1; 6373 2.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.1; 12418 -1.7; 13660 -1.3; 15026 -1.8; 16529 -4.5; 18182 -6.7; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.24 | 4.8 dB  |
| Peaking | 189 Hz   | 1.25 | -1.1 dB |
| Peaking | 2006 Hz  | 2.54 | 3.6 dB  |
| Peaking | 3865 Hz  | 2.27 | 5.1 dB  |
| Peaking | 4765 Hz  | 3.82 | 3.1 dB  |
| Peaking | 392 Hz   | 4.37 | 0.9 dB  |
| Peaking | 654 Hz   | 0.47 | -0.3 dB |
| Peaking | 1239 Hz  | 7.68 | 1.3 dB  |
| Peaking | 6717 Hz  | 9.27 | 3.3 dB  |
| Peaking | 19354 Hz | 0.94 | -8.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2/Audeze%20LCD-2.png)
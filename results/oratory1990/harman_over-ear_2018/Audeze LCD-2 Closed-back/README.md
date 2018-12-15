# Audeze LCD-2 Closed-back

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.7; 60 5.1; 66 4.6; 72 4.3; 79 3.8; 87 3.2; 96 2.4; 106 1.5; 116 0.8; 128 0.0; 141 -0.6; 155 -1.0; 170 -1.5; 187 -1.8; 206 -2.0; 227 -1.8; 249 -1.4; 274 -0.9; 302 -0.0; 332 0.8; 365 1.5; 402 1.5; 442 1.2; 486 0.9; 535 0.7; 588 0.6; 647 0.7; 712 0.8; 783 1.0; 861 0.6; 947 0.3; 1042 -0.3; 1146 -0.6; 1261 -0.5; 1387 -1.4; 1526 -2.4; 1678 -2.3; 1846 -2.6; 2031 -2.9; 2234 -1.8; 2457 -1.4; 2703 0.5; 2973 2.7; 3270 5.6; 3597 6.0; 3957 6.0; 4353 5.8; 4788 2.6; 5267 0.8; 5793 -3.2; 6373 -4.1; 7010 -4.7; 7711 -3.7; 8482 0.0; 9330 0.0; 10263 -0.4; 11289 -6.6; 12418 -6.4; 13660 -3.6; 15026 -2.6; 16529 -4.3; 18182 -10.4; 20000 -21.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Closed-back GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Closed-back ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.72 | 7.0 dB   |
| Peaking | 2101 Hz  | 1.54 | -4.8 dB  |
| Peaking | 3828 Hz  | 1.38 | 8.6 dB   |
| Peaking | 6372 Hz  | 2.23 | -6.6 dB  |
| Peaking | 20072 Hz | 1.17 | -21.3 dB |
| Peaking | 191 Hz   | 0.93 | -7.1 dB  |
| Peaking | 206 Hz   | 0.46 | 4.5 dB   |
| Peaking | 9869 Hz  | 3    | 4.8 dB   |
| Peaking | 11629 Hz | 2.66 | -7.5 dB  |
| Peaking | 15631 Hz | 2.07 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2%20Closed-back/Audeze%20LCD-2%20Closed-back.png)
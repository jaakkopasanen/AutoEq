# Shure SE215

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 -3.4; 23 -3.6; 25 -3.7; 28 -3.9; 31 -4.0; 34 -4.1; 37 -4.2; 41 -4.4; 45 -4.5; 49 -4.6; 54 -4.8; 60 -5.0; 66 -5.3; 72 -5.5; 79 -5.7; 87 -6.0; 96 -6.3; 106 -6.5; 116 -6.7; 128 -6.8; 141 -6.8; 155 -6.8; 170 -6.7; 187 -6.5; 206 -6.2; 227 -5.9; 249 -5.6; 274 -5.2; 302 -4.7; 332 -4.1; 365 -3.5; 402 -3.0; 442 -2.5; 486 -2.0; 535 -1.5; 588 -1.0; 647 -0.5; 712 -0.1; 783 0.3; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -0.7; 1387 -0.5; 1526 -0.7; 1678 -0.9; 1846 -1.2; 2031 -1.5; 2234 -1.3; 2457 -0.3; 2703 1.6; 2973 3.3; 3270 4.3; 3597 4.1; 3957 2.9; 4353 0.3; 4788 -3.4; 5267 -2.0; 5793 2.9; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 0.0; 11289 -0.3; 12418 -2.7; 13660 -5.4; 15026 -9.3; 16529 -12.1; 18182 -11.7; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.26 | -4.0 dB  |
| Peaking | 181 Hz   | 0.63 | -4.5 dB  |
| Peaking | 3352 Hz  | 4.48 | 4.9 dB   |
| Peaking | 10742 Hz | 0.68 | 6.9 dB   |
| Peaking | 16953 Hz | 0.55 | -14.9 dB |
| Peaking | 797 Hz   | 3.07 | 1.3 dB   |
| Peaking | 2038 Hz  | 2.19 | -2.1 dB  |
| Peaking | 5041 Hz  | 3.74 | -10.2 dB |
| Peaking | 6275 Hz  | 1.38 | 11.1 dB  |
| Peaking | 7678 Hz  | 1.72 | -7.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE215/Shure%20SE215.png)
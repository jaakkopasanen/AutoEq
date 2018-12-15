# Shure KSE1500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.9; 72 4.3; 79 3.5; 87 2.8; 96 2.1; 106 1.4; 116 0.7; 128 0.2; 141 -0.3; 155 -0.6; 170 -1.0; 187 -1.3; 206 -1.5; 227 -1.6; 249 -1.6; 274 -1.3; 302 -0.8; 332 -0.4; 365 -0.1; 402 0.1; 442 0.4; 486 0.6; 535 0.8; 588 1.0; 647 1.1; 712 1.2; 783 1.2; 861 1.0; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.6; 1387 -2.1; 1526 -2.3; 1678 -2.5; 1846 -2.5; 2031 -1.8; 2234 0.0; 2457 2.6; 2703 5.1; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.5; 9330 -10.1; 10263 -12.0; 11289 -8.2; 12418 -3.4; 13660 -4.2; 15026 -10.2; 16529 -15.8; 18182 -19.9; 20000 -22.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.38 | 6.5 dB   |
| Peaking | 169 Hz   | 1.01 | -3.1 dB  |
| Peaking | 1760 Hz  | 1.97 | -5.5 dB  |
| Peaking | 4262 Hz  | 0.77 | 9.3 dB   |
| Peaking | 20001 Hz | 0.4  | -23.0 dB |
| Peaking | 4443 Hz  | 2.2  | -3.7 dB  |
| Peaking | 6847 Hz  | 0.87 | 5.3 dB   |
| Peaking | 9966 Hz  | 2.19 | -13.2 dB |
| Peaking | 13049 Hz | 2.13 | 9.0 dB   |
| Peaking | 16986 Hz | 1.89 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20KSE1500/Shure%20KSE1500.png)
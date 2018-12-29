# Shure KSE1500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.2; 25 -1.3; 28 -1.3; 31 -1.4; 34 -1.4; 37 -1.5; 41 -1.6; 45 -1.6; 49 -1.7; 54 -1.8; 60 -2.0; 66 -2.2; 72 -2.3; 79 -2.5; 87 -2.7; 96 -2.8; 106 -3.0; 116 -3.0; 128 -3.0; 141 -2.9; 155 -2.7; 170 -2.5; 187 -2.3; 206 -2.1; 227 -1.9; 249 -1.6; 274 -1.3; 302 -0.8; 332 -0.4; 365 -0.1; 402 0.1; 442 0.4; 486 0.6; 535 0.8; 588 1.0; 647 1.1; 712 1.2; 783 1.2; 861 1.0; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.6; 1387 -2.1; 1526 -2.3; 1678 -2.5; 1846 -2.5; 2031 -1.8; 2234 0.0; 2457 2.6; 2703 5.1; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.5; 9330 -10.1; 10263 -12.0; 11289 -8.2; 12418 -3.4; 13660 -4.2; 15026 -10.2; 16529 -15.8; 18182 -19.9; 20000 -22.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.49 | -1.6 dB  |
| Peaking | 137 Hz   | 1.01 | -2.5 dB  |
| Peaking | 1764 Hz  | 1.99 | -5.5 dB  |
| Peaking | 4253 Hz  | 0.77 | 9.2 dB   |
| Peaking | 19984 Hz | 0.4  | -23.0 dB |
| Peaking | 649 Hz   | 1.98 | 1.4 dB   |
| Peaking | 6800 Hz  | 1.9  | 5.1 dB   |
| Peaking | 10019 Hz | 3.07 | -9.1 dB  |
| Peaking | 11904 Hz | 0.42 | -3.2 dB  |
| Peaking | 13178 Hz | 2.05 | 10.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20KSE1500/Shure%20KSE1500.png)
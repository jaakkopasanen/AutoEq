# Shure KSE1500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.4; 25 -7.4; 28 -7.5; 31 -7.5; 34 -7.6; 37 -7.7; 41 -7.8; 45 -7.8; 49 -7.9; 54 -8.0; 60 -8.2; 66 -8.3; 72 -8.5; 79 -8.7; 87 -8.8; 96 -9.0; 106 -9.1; 116 -9.2; 128 -9.2; 141 -9.1; 155 -8.9; 170 -8.7; 187 -8.5; 206 -8.3; 227 -8.0; 249 -7.8; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.6; 402 -6.4; 442 -6.1; 486 -5.9; 535 -5.8; 588 -5.7; 647 -5.5; 712 -5.5; 783 -5.4; 861 -5.6; 947 -6.1; 1042 -6.8; 1146 -7.7; 1261 -8.5; 1387 -9.2; 1526 -9.7; 1678 -10.0; 1846 -10.0; 2031 -9.7; 2234 -8.5; 2457 -6.4; 2703 -4.3; 2973 -2.5; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.2; 6373 -2.7; 7010 -4.6; 7711 -7.7; 8482 -12.6; 9330 -16.4; 10263 -17.1; 11289 -14.1; 12418 -8.2; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.8; 20000 -18.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 42 Hz   | 0.35 | -0.8 dB  |
| Peaking | 134 Hz  | 0.71 | -2.4 dB  |
| Peaking | 1878 Hz | 0.87 | -14.5 dB |
| Peaking | 3357 Hz | 0.32 | 13.0 dB  |
| Peaking | 9759 Hz | 1.67 | -17.5 dB |
| Peaking | 854 Hz  | 1.42 | 1.2 dB   |
| Peaking | 1316 Hz | 0.96 | -1.4 dB  |
| Peaking | 1732 Hz | 3.78 | 1.5 dB   |
| Peaking | 7580 Hz | 1.62 | 1.0 dB   |
| Peaking | 8350 Hz | 4.42 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 10.7 dB |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20KSE1500/Shure%20KSE1500.png)
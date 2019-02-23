# Shure KSE1500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.4; 28 -7.4; 31 -7.5; 34 -7.6; 37 -7.6; 41 -7.7; 45 -7.8; 49 -7.9; 54 -8.0; 60 -8.1; 66 -8.3; 72 -8.4; 79 -8.6; 87 -8.8; 96 -8.9; 106 -9.1; 116 -9.1; 128 -9.1; 141 -9.0; 155 -8.8; 170 -8.6; 187 -8.5; 206 -8.2; 227 -8.0; 249 -7.7; 274 -7.4; 302 -7.0; 332 -6.7; 365 -6.5; 402 -6.3; 442 -6.1; 486 -5.9; 535 -5.7; 588 -5.6; 647 -5.5; 712 -5.4; 783 -5.4; 861 -5.6; 947 -6.0; 1042 -6.7; 1146 -7.6; 1261 -8.4; 1387 -9.2; 1526 -9.6; 1678 -9.9; 1846 -10.0; 2031 -9.6; 2234 -8.4; 2457 -6.3; 2703 -4.2; 2973 -2.4; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.2; 6373 -2.6; 7010 -4.6; 7711 -7.7; 8482 -12.5; 9330 -16.4; 10263 -17.0; 11289 -14.1; 12418 -8.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.7; 20000 -18.2
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

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.36 | -0.8 dB  |
| Peaking | 134 Hz   | 0.72 | -2.4 dB  |
| Peaking | 1876 Hz  | 0.88 | -14.4 dB |
| Peaking | 3355 Hz  | 0.32 | 12.9 dB  |
| Peaking | 9758 Hz  | 1.68 | -17.4 dB |
| Peaking | 790 Hz   | 1.92 | 0.5 dB   |
| Peaking | 1226 Hz  | 4.09 | -0.9 dB  |
| Peaking | 5943 Hz  | 4.91 | 0.6 dB   |
| Peaking | 16391 Hz | 0.95 | 3.8 dB   |
| Peaking | 20026 Hz | 0.67 | -11.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 10.7 dB |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20KSE1500/Shure%20KSE1500.png)
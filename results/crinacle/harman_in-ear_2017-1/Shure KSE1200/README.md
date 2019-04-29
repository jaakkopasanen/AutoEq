# Shure KSE1200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.8; 28 -8.0; 31 -8.2; 34 -8.3; 37 -8.4; 41 -8.5; 45 -8.6; 49 -8.7; 54 -8.9; 60 -9.0; 66 -9.2; 72 -9.5; 79 -9.7; 87 -9.8; 96 -10.1; 106 -10.2; 116 -10.4; 128 -10.5; 141 -10.5; 155 -10.5; 170 -10.4; 187 -10.2; 206 -10.0; 227 -9.8; 249 -9.5; 274 -9.2; 302 -8.8; 332 -8.4; 365 -8.0; 402 -7.7; 442 -7.5; 486 -7.2; 535 -6.9; 588 -6.7; 647 -6.6; 712 -6.4; 783 -6.2; 861 -6.3; 947 -6.6; 1042 -7.4; 1146 -8.5; 1261 -9.6; 1387 -10.4; 1526 -10.9; 1678 -11.2; 1846 -10.9; 2031 -9.3; 2234 -6.4; 2457 -3.0; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -4.0; 7711 -7.9; 8482 -13.4; 9330 -15.3; 10263 -10.8; 11289 -6.5; 12418 -6.5; 13660 -9.9; 15026 -23.5; 16529 -31.3; 18182 -33.1; 20000 -29.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 124 Hz   | 0.47 | -4.1 dB  |
| Peaking | 1737 Hz  | 1.66 | -9.3 dB  |
| Peaking | 3391 Hz  | 0.72 | 8.7 dB   |
| Peaking | 16923 Hz | 1.85 | -16.8 dB |
| Peaking | 21861 Hz | 0.86 | -23.7 dB |
| Peaking | 759 Hz   | 2.09 | 1.1 dB   |
| Peaking | 3011 Hz  | 1    | 3.0 dB   |
| Peaking | 6010 Hz  | 2.15 | 8.9 dB   |
| Peaking | 12804 Hz | 1.67 | 18.3 dB  |
| Peaking | 19789 Hz | 0.08 | -19.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 10.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -28.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20KSE1200/Shure%20KSE1200.png)
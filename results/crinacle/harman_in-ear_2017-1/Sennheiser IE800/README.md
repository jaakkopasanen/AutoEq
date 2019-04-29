# Sennheiser IE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.1; 25 -8.1; 28 -8.0; 31 -8.0; 34 -8.0; 37 -8.0; 41 -8.0; 45 -7.9; 49 -7.8; 54 -7.8; 60 -7.8; 66 -7.9; 72 -8.1; 79 -8.3; 87 -8.4; 96 -8.7; 106 -8.9; 116 -9.2; 128 -9.4; 141 -9.5; 155 -9.7; 170 -9.8; 187 -9.9; 206 -10.0; 227 -10.0; 249 -10.0; 274 -10.0; 302 -9.9; 332 -9.8; 365 -9.6; 402 -9.6; 442 -9.6; 486 -9.5; 535 -9.4; 588 -9.3; 647 -9.2; 712 -9.0; 783 -8.8; 861 -8.7; 947 -8.8; 1042 -9.2; 1146 -9.6; 1261 -10.0; 1387 -9.7; 1526 -8.9; 1678 -7.7; 1846 -6.2; 2031 -4.2; 2234 -2.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -4.0; 5793 -6.6; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.9; 10263 -10.2; 11289 -7.7; 12418 -9.5; 13660 -19.8; 15026 -30.8; 16529 -34.2; 18182 -30.5; 20000 -24.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 410 Hz   | 0.27 | -5.1 dB  |
| Peaking | 1360 Hz  | 1.14 | -8.1 dB  |
| Peaking | 4491 Hz  | 0.24 | 18.1 dB  |
| Peaking | 12051 Hz | 2.06 | 12.8 dB  |
| Peaking | 16041 Hz | 0.34 | -36.4 dB |
| Peaking | 25 Hz    | 1.17 | -1.4 dB  |
| Peaking | 1821 Hz  | 4.81 | -1.0 dB  |
| Peaking | 2401 Hz  | 5.44 | 1.6 dB   |
| Peaking | 5707 Hz  | 6.69 | -6.1 dB  |
| Peaking | 6392 Hz  | 4.38 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 16000 Hz | 1.41 | -35.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE800/Sennheiser%20IE800.png)
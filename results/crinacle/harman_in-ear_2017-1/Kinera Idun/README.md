# Kinera Idun
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.7; 25 -3.9; 28 -4.1; 31 -4.3; 34 -4.4; 37 -4.6; 41 -4.8; 45 -5.0; 49 -5.2; 54 -5.4; 60 -5.6; 66 -5.9; 72 -6.2; 79 -6.5; 87 -6.9; 96 -7.3; 106 -7.7; 116 -8.0; 128 -8.3; 141 -8.6; 155 -8.7; 170 -8.8; 187 -8.8; 206 -8.8; 227 -8.7; 249 -8.6; 274 -8.4; 302 -8.0; 332 -7.6; 365 -7.1; 402 -6.7; 442 -6.2; 486 -5.7; 535 -5.4; 588 -5.1; 647 -4.9; 712 -4.6; 783 -4.6; 861 -4.9; 947 -5.8; 1042 -7.4; 1146 -8.9; 1261 -9.6; 1387 -9.6; 1526 -8.9; 1678 -7.6; 1846 -6.0; 2031 -4.4; 2234 -3.0; 2457 -2.4; 2703 -2.6; 2973 -3.3; 3270 -3.6; 3597 -2.8; 3957 -2.1; 4353 -1.2; 4788 -0.5; 5267 -2.4; 5793 -3.9; 6373 -3.3; 7010 -4.1; 7711 -5.8; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.9; 12418 -8.0; 13660 -13.0; 15026 -19.5; 16529 -22.1; 18182 -20.5; 20000 -19.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Idun GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Idun ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 201 Hz   | 0.81 | -3.6 dB  |
| Peaking | 1373 Hz  | 1.79 | -7.5 dB  |
| Peaking | 2385 Hz  | 6.45 | 1.4 dB   |
| Peaking | 11015 Hz | 0.15 | 24.0 dB  |
| Peaking | 16501 Hz | 0.21 | -36.8 dB |
| Peaking | 23 Hz    | 0.89 | 2.3 dB   |
| Peaking | 3235 Hz  | 6.48 | -1.1 dB  |
| Peaking | 4641 Hz  | 5.72 | 2.5 dB   |
| Peaking | 7972 Hz  | 2.23 | -2.0 dB  |
| Peaking | 11717 Hz | 3.59 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB   |
| Peaking | 62 Hz    | 1.41 | 0.2 dB   |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -19.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kinera%20Idun/Kinera%20Idun.png)
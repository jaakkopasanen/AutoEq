# Tin Audio T2 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.2; 66 -1.6; 72 -2.1; 79 -2.7; 87 -3.3; 96 -3.9; 106 -4.5; 116 -5.1; 128 -5.7; 141 -6.2; 155 -6.7; 170 -7.1; 187 -7.4; 206 -7.7; 227 -8.0; 249 -8.1; 274 -8.2; 302 -8.2; 332 -8.1; 365 -8.1; 402 -7.9; 442 -7.7; 486 -7.4; 535 -7.1; 588 -6.7; 647 -6.2; 712 -5.6; 783 -5.0; 861 -4.4; 947 -4.1; 1042 -4.2; 1146 -4.6; 1261 -5.0; 1387 -5.3; 1526 -5.2; 1678 -4.9; 1846 -4.6; 2031 -4.6; 2234 -4.9; 2457 -5.1; 2703 -5.0; 2973 -4.2; 3270 -3.4; 3597 -3.3; 3957 -3.7; 4353 -4.7; 4788 -6.5; 5267 -7.0; 5793 -5.4; 6373 -4.9; 7010 -9.0; 7711 -15.2; 8482 -16.3; 9330 -12.9; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.6; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.7  | 7.0 dB   |
| Peaking | 1010 Hz  | 2.52 | 2.5 dB   |
| Peaking | 3358 Hz  | 1.33 | 3.1 dB   |
| Peaking | 6397 Hz  | 6.31 | 4.1 dB   |
| Peaking | 8216 Hz  | 3.15 | -11.5 dB |
| Peaking | 32 Hz    | 0.27 | 3.7 dB   |
| Peaking | 35 Hz    | 1.16 | -4.5 dB  |
| Peaking | 285 Hz   | 0.43 | -3.1 dB  |
| Peaking | 701 Hz   | 0.66 | 1.6 dB   |
| Peaking | 10951 Hz | 5.87 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Tin%20Audio%20T2%20Pro/Tin%20Audio%20T2%20Pro.png)
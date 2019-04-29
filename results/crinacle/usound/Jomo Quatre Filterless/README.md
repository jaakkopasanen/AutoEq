# Jomo Quatre Filterless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.0; 25 -8.1; 28 -8.3; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.8; 45 -9.0; 49 -9.1; 54 -9.3; 60 -9.6; 66 -9.8; 72 -10.1; 79 -10.4; 87 -10.8; 96 -11.2; 106 -11.5; 116 -11.7; 128 -11.9; 141 -12.1; 155 -12.2; 170 -12.3; 187 -12.3; 206 -12.1; 227 -12.0; 249 -11.8; 274 -11.5; 302 -11.2; 332 -10.9; 365 -10.7; 402 -10.3; 442 -9.9; 486 -9.4; 535 -8.9; 588 -8.4; 647 -7.8; 712 -7.1; 783 -6.4; 861 -5.7; 947 -5.4; 1042 -5.3; 1146 -5.6; 1261 -5.7; 1387 -5.2; 1526 -4.3; 1678 -3.8; 1846 -3.1; 2031 -2.8; 2234 -2.7; 2457 -1.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.7; 4788 -6.4; 5267 -5.7; 5793 -2.0; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Quatre Filterless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Quatre Filterless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.24 | -1.6 dB |
| Peaking | 170 Hz  | 0.57 | -4.4 dB |
| Peaking | 406 Hz  | 1.05 | -1.9 dB |
| Peaking | 2503 Hz | 0.39 | 2.3 dB  |
| Peaking | 3159 Hz | 1.57 | 4.3 dB  |
| Peaking | 1290 Hz | 8.36 | -1.0 dB |
| Peaking | 4090 Hz | 6.07 | 2.4 dB  |
| Peaking | 4948 Hz | 4.23 | -4.8 dB |
| Peaking | 6250 Hz | 2.93 | 6.8 dB  |
| Peaking | 7363 Hz | 1.54 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Quatre%20Filterless/Jomo%20Quatre%20Filterless.png)
# FitEar TG334 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -5.8; 25 -5.8; 28 -5.9; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.3; 45 -6.5; 49 -6.6; 54 -6.9; 60 -7.1; 66 -7.4; 72 -7.7; 79 -8.1; 87 -8.5; 96 -9.0; 106 -9.4; 116 -9.6; 128 -9.9; 141 -10.3; 155 -10.5; 170 -10.6; 187 -10.7; 206 -10.7; 227 -10.6; 249 -10.5; 274 -10.3; 302 -10.1; 332 -9.9; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.6; 535 -8.2; 588 -7.8; 647 -7.3; 712 -6.7; 783 -6.2; 861 -5.7; 947 -5.5; 1042 -5.7; 1146 -6.2; 1261 -6.8; 1387 -7.2; 1526 -7.0; 1678 -6.3; 1846 -5.1; 2031 -3.9; 2234 -3.3; 2457 -2.8; 2703 -1.6; 2973 -1.2; 3270 -1.8; 3597 -2.2; 3957 -2.0; 4353 -0.9; 4788 -0.5; 5267 -2.4; 5793 -5.0; 6373 -6.9; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 212 Hz  | 0.55 | -4.3 dB |
| Peaking | 879 Hz  | 3.34 | 1.7 dB  |
| Peaking | 2835 Hz | 1.95 | 4.7 dB  |
| Peaking | 4786 Hz | 2.39 | 6.0 dB  |
| Peaking | 6058 Hz | 3.26 | -2.2 dB |
| Peaking | 28 Hz   | 1    | 0.9 dB  |
| Peaking | 1493 Hz | 4.12 | -1.3 dB |
| Peaking | 2043 Hz | 6.22 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20TG334%20sample%201/FitEar%20TG334%20sample%201.png)
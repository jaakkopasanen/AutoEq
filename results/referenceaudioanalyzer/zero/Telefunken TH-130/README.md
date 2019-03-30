# Telefunken TH-130
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.4; 25 -14.5; 28 -14.5; 31 -14.5; 34 -14.4; 37 -14.3; 41 -14.0; 45 -13.8; 49 -13.5; 54 -13.2; 60 -12.8; 66 -12.4; 72 -11.9; 79 -11.5; 87 -11.0; 96 -10.4; 106 -9.8; 116 -9.2; 128 -8.6; 141 -8.0; 155 -7.4; 170 -6.8; 187 -6.2; 206 -5.6; 227 -5.1; 249 -5.0; 274 -4.7; 302 -4.2; 332 -3.6; 365 -3.1; 402 -2.7; 442 -2.3; 486 -1.9; 535 -1.6; 588 -1.3; 647 -1.0; 712 -0.8; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.7; 1526 -1.4; 1678 -2.2; 1846 -3.2; 2031 -4.6; 2234 -6.2; 2457 -7.8; 2703 -8.6; 2973 -8.7; 3270 -8.1; 3597 -6.7; 3957 -5.0; 4353 -4.4; 4788 -5.2; 5267 -7.3; 5793 -9.0; 6373 -8.3; 7010 -4.6; 7711 -4.1; 8482 -4.4; 9330 -4.4; 10263 -4.8; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Telefunken TH-130 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Telefunken TH-130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.15 | -11.3 dB |
| Peaking | 512 Hz   | 0.11 | 5.4 dB   |
| Peaking | 2737 Hz  | 1.6  | -8.3 dB  |
| Peaking | 6044 Hz  | 3.09 | -6.2 dB  |
| Peaking | 7228 Hz  | 4.89 | 1.9 dB   |
| Peaking | 385 Hz   | 1.87 | -0.4 dB  |
| Peaking | 1356 Hz  | 5.7  | 0.5 dB   |
| Peaking | 3405 Hz  | 6.91 | -1.0 dB  |
| Peaking | 4250 Hz  | 7.38 | 0.9 dB   |
| Peaking | 10062 Hz | 4.95 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Telefunken%20TH-130/Telefunken%20TH-130.png)
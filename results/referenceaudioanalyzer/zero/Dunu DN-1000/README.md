# Dunu DN-1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.0; 25 -11.0; 28 -11.1; 31 -11.1; 34 -11.0; 37 -11.0; 41 -10.9; 45 -10.8; 49 -10.7; 54 -10.6; 60 -10.4; 66 -10.2; 72 -10.1; 79 -9.9; 87 -9.6; 96 -9.4; 106 -9.1; 116 -8.8; 128 -8.4; 141 -8.0; 155 -7.6; 170 -7.2; 187 -6.8; 206 -6.5; 227 -6.4; 249 -6.1; 274 -5.7; 302 -5.3; 332 -5.0; 365 -4.6; 402 -4.3; 442 -4.0; 486 -3.7; 535 -3.5; 588 -3.3; 647 -3.1; 712 -2.9; 783 -2.9; 861 -2.6; 947 -2.6; 1042 -2.6; 1146 -2.3; 1261 -2.2; 1387 -1.9; 1526 -1.6; 1678 -1.3; 1846 -1.3; 2031 -1.5; 2234 -2.1; 2457 -2.9; 2703 -4.1; 2973 -4.5; 3270 -3.1; 3597 -0.5; 3957 -0.5; 4353 -3.5; 4788 -4.9; 5267 -4.0; 5793 -2.7; 6373 -1.9; 7010 -1.2; 7711 -3.2; 8482 -3.4; 9330 -3.4; 10263 -3.5; 11289 -3.5; 12418 -3.5; 13660 -3.5; 15026 -3.5; 16529 -3.5; 18182 -3.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN-1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN-1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.16 | -7.6 dB |
| Peaking | 2887 Hz  | 0.47 | 4.6 dB  |
| Peaking | 3570 Hz  | 1.23 | -8.6 dB |
| Peaking | 3720 Hz  | 4.34 | 8.2 dB  |
| Peaking | 22050 Hz | 1.92 | 0.2 dB  |
| Peaking | 1220 Hz  | 3.3  | -0.4 dB |
| Peaking | 1848 Hz  | 4.19 | 0.5 dB  |
| Peaking | 4902 Hz  | 8.31 | -1.3 dB |
| Peaking | 6783 Hz  | 3.64 | 2.7 dB  |
| Peaking | 7967 Hz  | 1.68 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20DN-1000/Dunu%20DN-1000.png)
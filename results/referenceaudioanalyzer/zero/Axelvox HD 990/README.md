# Axelvox HD 990
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -2.0; 25 -3.2; 28 -4.8; 31 -6.1; 34 -7.1; 37 -7.9; 41 -8.6; 45 -9.0; 49 -9.2; 54 -9.3; 60 -9.5; 66 -9.7; 72 -9.7; 79 -9.5; 87 -9.2; 96 -9.0; 106 -8.8; 116 -8.5; 128 -8.2; 141 -7.8; 155 -7.5; 170 -7.1; 187 -6.7; 206 -6.2; 227 -5.7; 249 -5.1; 274 -4.8; 302 -4.8; 332 -5.1; 365 -5.1; 402 -5.1; 442 -5.1; 486 -5.1; 535 -4.5; 588 -3.6; 647 -3.6; 712 -4.3; 783 -4.5; 861 -4.5; 947 -4.4; 1042 -4.2; 1146 -3.8; 1261 -3.3; 1387 -2.9; 1526 -2.4; 1678 -2.2; 1846 -2.5; 2031 -3.3; 2234 -4.0; 2457 -4.1; 2703 -3.1; 2973 -0.9; 3270 -0.5; 3597 -2.6; 3957 -3.8; 4353 -3.7; 4788 -2.8; 5267 -1.4; 5793 -0.6; 6373 -3.1; 7010 -7.6; 7711 -9.8; 8482 -8.5; 9330 -5.7; 10263 -5.6; 11289 -8.3; 12418 -9.3; 13660 -6.0; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Axelvox HD 990 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Axelvox HD 990 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.83 | 6.3 dB  |
| Peaking | 64 Hz    | 0.52 | -5.4 dB |
| Peaking | 5563 Hz  | 0.29 | 3.0 dB  |
| Peaking | 7807 Hz  | 3.73 | -8.2 dB |
| Peaking | 12122 Hz | 2.4  | -6.7 dB |
| Peaking | 1642 Hz  | 2.76 | 1.7 dB  |
| Peaking | 2434 Hz  | 3.11 | -1.4 dB |
| Peaking | 3174 Hz  | 3.73 | 4.7 dB  |
| Peaking | 3766 Hz  | 0.99 | -2.9 dB |
| Peaking | 5619 Hz  | 4.21 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Axelvox%20HD%20990/Axelvox%20HD%20990.png)
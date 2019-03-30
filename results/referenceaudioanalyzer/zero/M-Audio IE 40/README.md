# M-Audio IE 40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.5; 25 -12.5; 28 -12.5; 31 -12.6; 34 -12.6; 37 -12.7; 41 -12.8; 45 -12.8; 49 -12.9; 54 -12.9; 60 -12.9; 66 -12.9; 72 -12.9; 79 -12.9; 87 -12.8; 96 -12.8; 106 -12.7; 116 -12.6; 128 -12.5; 141 -12.5; 155 -12.2; 170 -12.2; 187 -12.0; 206 -11.8; 227 -11.6; 249 -11.6; 274 -11.6; 302 -11.5; 332 -11.2; 365 -11.1; 402 -10.9; 442 -10.9; 486 -10.6; 535 -10.2; 588 -9.8; 647 -9.4; 712 -8.9; 783 -8.4; 861 -7.9; 947 -7.4; 1042 -6.8; 1146 -6.2; 1261 -5.6; 1387 -5.2; 1526 -4.8; 1678 -4.4; 1846 -4.3; 2031 -4.6; 2234 -5.0; 2457 -5.0; 2703 -4.5; 2973 -3.4; 3270 -2.2; 3597 -1.3; 3957 -1.2; 4353 -1.2; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`M-Audio IE 40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `M-Audio IE 40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.08 | -6.2 dB |
| Peaking | 1457 Hz | 1.52 | 2.1 dB  |
| Peaking | 5421 Hz | 0.86 | 7.8 dB  |
| Peaking | 8483 Hz | 1.36 | -4.3 dB |
| Peaking | 2592 Hz | 2.94 | -1.7 dB |
| Peaking | 4002 Hz | 1.08 | 2.2 dB  |
| Peaking | 4621 Hz | 2.54 | -2.7 dB |
| Peaking | 7468 Hz | 7.56 | -1.6 dB |
| Peaking | 9267 Hz | 4.87 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/M-Audio%20IE%2040/M-Audio%20IE%2040.png)
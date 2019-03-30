# Denon AH-A100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -1.0; 41 -1.6; 45 -2.0; 49 -2.3; 54 -2.5; 60 -2.8; 66 -3.2; 72 -3.9; 79 -4.6; 87 -5.2; 96 -5.8; 106 -6.2; 116 -6.7; 128 -7.1; 141 -7.1; 155 -6.9; 170 -6.8; 187 -6.9; 206 -6.9; 227 -6.9; 249 -6.9; 274 -6.9; 302 -6.9; 332 -6.9; 365 -7.1; 402 -7.8; 442 -8.7; 486 -9.3; 535 -9.7; 588 -9.8; 647 -9.8; 712 -9.4; 783 -8.8; 861 -8.1; 947 -7.3; 1042 -6.4; 1146 -5.7; 1261 -5.1; 1387 -4.9; 1526 -4.7; 1678 -5.1; 1846 -5.9; 2031 -6.5; 2234 -7.0; 2457 -7.2; 2703 -6.5; 2973 -4.0; 3270 -3.0; 3597 -4.1; 3957 -4.6; 4353 -3.6; 4788 -1.2; 5267 -0.5; 5793 -2.1; 6373 -7.7; 7010 -9.0; 7711 -8.2; 8482 -7.5; 9330 -8.2; 10263 -9.1; 11289 -9.1; 12418 -8.1; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-A100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-A100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.73 | 6.5 dB   |
| Peaking | 608 Hz   | 1.26 | -3.6 dB  |
| Peaking | 1344 Hz  | 2.41 | 2.3 dB   |
| Peaking | 5443 Hz  | 1.38 | 19.4 dB  |
| Peaking | 6200 Hz  | 0.98 | -14.9 dB |
| Peaking | 132 Hz   | 3.06 | -1.3 dB  |
| Peaking | 2490 Hz  | 3.63 | -1.8 dB  |
| Peaking | 3160 Hz  | 6.29 | 2.9 dB   |
| Peaking | 8493 Hz  | 5.44 | 1.6 dB   |
| Peaking | 10925 Hz | 3.32 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-A100/Denon%20AH-A100.png)
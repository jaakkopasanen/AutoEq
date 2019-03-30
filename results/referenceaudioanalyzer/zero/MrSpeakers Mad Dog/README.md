# MrSpeakers Mad Dog
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -10.0; 28 -10.0; 31 -10.1; 34 -10.0; 37 -10.0; 41 -9.9; 45 -10.0; 49 -10.3; 54 -10.9; 60 -11.4; 66 -11.4; 72 -11.3; 79 -10.9; 87 -10.2; 96 -9.5; 106 -8.7; 116 -8.4; 128 -8.8; 141 -9.1; 155 -9.1; 170 -9.0; 187 -9.0; 206 -9.1; 227 -9.1; 249 -9.1; 274 -9.0; 302 -8.7; 332 -8.5; 365 -8.5; 402 -8.8; 442 -8.8; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.8; 712 -8.0; 783 -7.8; 861 -7.7; 947 -7.2; 1042 -6.6; 1146 -5.9; 1261 -5.1; 1387 -4.3; 1526 -4.0; 1678 -3.8; 1846 -3.2; 2031 -2.1; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -2.0; 3957 -3.0; 4353 -2.8; 4788 -1.6; 5267 -1.3; 5793 -2.9; 6373 -7.0; 7010 -10.8; 7711 -12.5; 8482 -12.1; 9330 -11.4; 10263 -11.8; 11289 -11.5; 12418 -8.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Mad Dog GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.04 | -2.6 dB |
| Peaking | 63 Hz    | 2.04 | -2.6 dB |
| Peaking | 2677 Hz  | 0.84 | 7.2 dB  |
| Peaking | 5477 Hz  | 2.56 | 7.7 dB  |
| Peaking | 7800 Hz  | 1    | -8.4 dB |
| Peaking | 25 Hz    | 1.48 | -0.8 dB |
| Peaking | 115 Hz   | 5.32 | 1.1 dB  |
| Peaking | 1345 Hz  | 6.79 | 0.8 dB  |
| Peaking | 11240 Hz | 3.3  | -3.7 dB |
| Peaking | 12976 Hz | 1.27 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MrSpeakers%20Mad%20Dog/MrSpeakers%20Mad%20Dog.png)
# Kinera BD005
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -14.6; 25 -14.6; 28 -14.6; 31 -14.6; 34 -14.6; 37 -14.6; 41 -14.6; 45 -14.6; 49 -14.6; 54 -14.6; 60 -14.6; 66 -14.6; 72 -14.4; 79 -14.3; 87 -14.3; 96 -14.3; 106 -14.1; 116 -14.0; 128 -13.9; 141 -13.6; 155 -13.5; 170 -13.3; 187 -13.0; 206 -12.7; 227 -12.3; 249 -12.0; 274 -11.5; 302 -11.2; 332 -11.0; 365 -10.6; 402 -10.1; 442 -9.6; 486 -9.0; 535 -8.4; 588 -7.8; 647 -7.1; 712 -6.4; 783 -5.7; 861 -5.1; 947 -4.5; 1042 -3.7; 1146 -2.7; 1261 -2.0; 1387 -2.0; 1526 -2.0; 1678 -2.4; 1846 -2.8; 2031 -3.0; 2234 -3.2; 2457 -3.6; 2703 -4.2; 2973 -5.1; 3270 -5.2; 3597 -3.9; 3957 -2.9; 4353 -4.8; 4788 -8.2; 5267 -8.8; 5793 -5.8; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera BD005 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera BD005 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.09 | -8.8 dB |
| Peaking | 1398 Hz | 0.91 | 4.8 dB  |
| Peaking | 4018 Hz | 4.99 | 3.7 dB  |
| Peaking | 5193 Hz | 2.75 | -5.1 dB |
| Peaking | 6368 Hz | 5.37 | 7.3 dB  |
| Peaking | 399 Hz  | 4.46 | -0.2 dB |
| Peaking | 2432 Hz | 5.16 | 0.5 dB  |
| Peaking | 3070 Hz | 7.07 | -0.8 dB |
| Peaking | 8027 Hz | 6.81 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Kinera%20BD005/Kinera%20BD005.png)
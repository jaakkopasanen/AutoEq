# Cardas EM5813
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.4; 25 -14.4; 28 -14.3; 31 -14.2; 34 -14.2; 37 -14.2; 41 -14.2; 45 -14.2; 49 -14.2; 54 -14.2; 60 -14.2; 66 -14.2; 72 -14.2; 79 -14.2; 87 -14.2; 96 -14.1; 106 -14.1; 116 -13.9; 128 -13.8; 141 -13.8; 155 -13.8; 170 -13.8; 187 -13.8; 206 -13.8; 227 -13.8; 249 -13.8; 274 -13.5; 302 -13.5; 332 -13.4; 365 -13.2; 402 -13.2; 442 -12.9; 486 -12.7; 535 -12.4; 588 -12.1; 647 -11.7; 712 -11.2; 783 -10.5; 861 -9.6; 947 -8.2; 1042 -6.6; 1146 -5.3; 1261 -4.4; 1387 -3.7; 1526 -2.8; 1678 -1.8; 1846 -1.2; 2031 -1.8; 2234 -4.8; 2457 -7.9; 2703 -8.8; 2973 -8.0; 3270 -6.5; 3597 -4.9; 3957 -3.1; 4353 -2.4; 4788 -2.8; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cardas EM5813 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.08 | -7.7 dB |
| Peaking | 680 Hz  | 0.58 | -4.8 dB |
| Peaking | 1966 Hz | 0.73 | 9.7 dB  |
| Peaking | 2644 Hz | 2.35 | -9.8 dB |
| Peaking | 5787 Hz | 3.08 | 5.0 dB  |
| Peaking | 1074 Hz | 2.11 | -1.2 dB |
| Peaking | 1140 Hz | 3.65 | 1.8 dB  |
| Peaking | 3306 Hz | 6.2  | -1.0 dB |
| Peaking | 4117 Hz | 5.56 | 1.7 dB  |
| Peaking | 8434 Hz | 3    | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -6.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Cardas%20EM5813/Cardas%20EM5813.png)
# Koss SportaPro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.3; 49 -3.4; 54 -4.5; 60 -5.7; 66 -6.6; 72 -7.2; 79 -7.8; 87 -8.3; 96 -8.7; 106 -9.0; 116 -9.1; 128 -9.1; 141 -9.0; 155 -8.8; 170 -8.5; 187 -8.1; 206 -7.8; 227 -7.4; 249 -7.0; 274 -6.7; 302 -6.3; 332 -6.0; 365 -5.6; 402 -5.3; 442 -5.0; 486 -4.7; 535 -4.4; 588 -4.2; 647 -3.9; 712 -3.7; 783 -3.5; 861 -3.5; 947 -3.3; 1042 -3.2; 1146 -3.3; 1261 -3.5; 1387 -3.6; 1526 -3.9; 1678 -4.2; 1846 -4.8; 2031 -5.4; 2234 -6.3; 2457 -7.4; 2703 -8.3; 2973 -8.8; 3270 -9.4; 3597 -9.5; 3957 -8.0; 4353 -4.5; 4788 -7.8; 5267 -13.2; 5793 -13.8; 6373 -10.8; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -9.4; 11289 -10.7; 12418 -10.5; 13660 -7.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss SportaPro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SportaPro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.61 | 7.3 dB  |
| Peaking | 1050 Hz  | 0.82 | 3.6 dB  |
| Peaking | 3109 Hz  | 2.94 | -3.6 dB |
| Peaking | 5656 Hz  | 5.42 | -8.4 dB |
| Peaking | 11723 Hz | 2.93 | -4.9 dB |
| Peaking | 44 Hz    | 3.14 | 2.5 dB  |
| Peaking | 119 Hz   | 1    | -3.2 dB |
| Peaking | 4451 Hz  | 6.93 | 6.6 dB  |
| Peaking | 4653 Hz  | 2.16 | -2.8 dB |
| Peaking | 7400 Hz  | 5.25 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Koss%20SportaPro/Koss%20SportaPro.png)
# Yamaha EPH-50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -14.0; 25 -14.4; 28 -14.8; 31 -15.0; 34 -15.2; 37 -15.3; 41 -15.4; 45 -15.5; 49 -15.6; 54 -15.7; 60 -15.5; 66 -15.3; 72 -15.3; 79 -15.1; 87 -14.9; 96 -14.6; 106 -14.2; 116 -13.8; 128 -13.2; 141 -12.3; 155 -11.7; 170 -12.1; 187 -12.7; 206 -12.4; 227 -11.7; 249 -10.9; 274 -10.1; 302 -9.3; 332 -8.5; 365 -7.7; 402 -6.9; 442 -6.1; 486 -5.1; 535 -4.1; 588 -3.0; 647 -1.9; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -1.2; 1678 -1.7; 1846 -2.0; 2031 -2.2; 2234 -2.8; 2457 -4.3; 2703 -6.1; 2973 -7.7; 3270 -9.2; 3597 -9.8; 3957 -9.3; 4353 -8.8; 4788 -9.3; 5267 -11.1; 5793 -12.7; 6373 -12.1; 7010 -8.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha EPH-50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha EPH-50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.69 | -5.1 dB |
| Peaking | 68 Hz   | 0.54 | -7.0 dB |
| Peaking | 261 Hz  | 0.65 | -5.0 dB |
| Peaking | 1033 Hz | 0.41 | 7.7 dB  |
| Peaking | 4421 Hz | 0.91 | -6.2 dB |
| Peaking | 2221 Hz | 4.6  | 1.4 dB  |
| Peaking | 3369 Hz | 2.15 | -2.1 dB |
| Peaking | 4472 Hz | 2.8  | 3.3 dB  |
| Peaking | 6215 Hz | 2.75 | -6.6 dB |
| Peaking | 7255 Hz | 2    | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20EPH-50/Yamaha%20EPH-50.png)
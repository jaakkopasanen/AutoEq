# Grado iGrado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.2; 60 -2.1; 66 -2.8; 72 -3.3; 79 -3.9; 87 -4.3; 96 -4.6; 106 -4.8; 116 -5.0; 128 -5.1; 141 -5.1; 155 -5.1; 170 -5.1; 187 -4.7; 206 -4.4; 227 -4.4; 249 -4.4; 274 -4.4; 302 -4.4; 332 -4.4; 365 -4.4; 402 -4.7; 442 -4.8; 486 -4.7; 535 -4.7; 588 -4.7; 647 -4.7; 712 -4.7; 783 -4.7; 861 -4.8; 947 -5.0; 1042 -5.2; 1146 -5.5; 1261 -5.8; 1387 -6.2; 1526 -6.7; 1678 -7.4; 1846 -8.2; 2031 -9.2; 2234 -10.3; 2457 -11.1; 2703 -11.3; 2973 -10.9; 3270 -9.9; 3597 -8.8; 3957 -8.7; 4353 -10.6; 4788 -12.4; 5267 -12.5; 5793 -10.7; 6373 -7.8; 7010 -5.0; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -10.3; 11289 -11.2; 12418 -9.9; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGrado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGrado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.62 | 6.6 dB  |
| Peaking | 574 Hz   | 0.32 | 2.0 dB  |
| Peaking | 2544 Hz  | 1.6  | -5.4 dB |
| Peaking | 5045 Hz  | 3.89 | -6.2 dB |
| Peaking | 11449 Hz | 3.32 | -5.2 dB |
| Peaking | 51 Hz    | 0.93 | -1.4 dB |
| Peaking | 53 Hz    | 2.16 | 2.2 dB  |
| Peaking | 6006 Hz  | 4.42 | -2.5 dB |
| Peaking | 6869 Hz  | 2.65 | 2.9 dB  |
| Peaking | 10176 Hz | 9.09 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | -4.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20iGrado/Grado%20iGrado.png)
# Sony MDR-ZX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.1; 72 -2.4; 79 -3.5; 87 -4.5; 96 -5.3; 106 -5.7; 116 -6.0; 128 -5.8; 141 -5.5; 155 -4.9; 170 -4.1; 187 -3.6; 206 -3.7; 227 -4.3; 249 -5.1; 274 -6.1; 302 -7.3; 332 -8.2; 365 -8.5; 402 -8.2; 442 -7.9; 486 -7.6; 535 -7.3; 588 -6.9; 647 -6.4; 712 -6.2; 783 -6.3; 861 -6.4; 947 -6.6; 1042 -6.8; 1146 -7.0; 1261 -7.3; 1387 -7.7; 1526 -8.1; 1678 -8.6; 1846 -9.0; 2031 -8.8; 2234 -7.8; 2457 -6.4; 2703 -5.7; 2973 -6.0; 3270 -6.0; 3597 -4.8; 3957 -2.3; 4353 -0.5; 4788 -0.5; 5267 -2.7; 5793 -3.7; 6373 -3.2; 7010 -6.1; 7711 -11.6; 8482 -15.9; 9330 -16.6; 10263 -13.3; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.69 | 6.9 dB   |
| Peaking | 196 Hz   | 4.36 | 2.8 dB   |
| Peaking | 1871 Hz  | 1.59 | -2.9 dB  |
| Peaking | 4910 Hz  | 1.39 | 6.6 dB   |
| Peaking | 8954 Hz  | 2.84 | -12.7 dB |
| Peaking | 63 Hz    | 4.25 | 2.0 dB   |
| Peaking | 107 Hz   | 3.42 | -1.3 dB  |
| Peaking | 375 Hz   | 3.11 | -2.4 dB  |
| Peaking | 10236 Hz | 5.62 | -3.3 dB  |
| Peaking | 11433 Hz | 2.49 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)
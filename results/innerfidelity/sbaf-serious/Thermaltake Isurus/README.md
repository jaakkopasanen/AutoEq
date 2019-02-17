# Thermaltake Isurus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -1.9; 25 -2.0; 28 -2.1; 31 -2.3; 34 -2.4; 37 -2.6; 41 -2.7; 45 -2.9; 49 -3.1; 54 -3.3; 60 -3.6; 66 -3.9; 72 -4.2; 79 -4.7; 87 -5.2; 96 -5.6; 106 -5.9; 116 -6.1; 128 -6.5; 141 -6.7; 155 -7.0; 170 -7.2; 187 -7.2; 206 -7.4; 227 -7.4; 249 -7.4; 274 -7.4; 302 -7.2; 332 -7.1; 365 -6.8; 402 -6.6; 442 -6.2; 486 -5.3; 535 -4.7; 588 -4.1; 647 -3.5; 712 -3.1; 783 -2.3; 861 -2.0; 947 -1.8; 1042 -1.6; 1146 -1.6; 1261 -1.6; 1387 -2.1; 1526 -2.7; 1678 -3.1; 1846 -3.3; 2031 -3.3; 2234 -3.2; 2457 -2.5; 2703 -2.3; 2973 -1.5; 3270 -0.9; 3597 -0.5; 3957 -1.1; 4353 -3.1; 4788 -3.7; 5267 -4.5; 5793 -5.6; 6373 -6.6; 7010 -4.6; 7711 -3.3; 8482 -4.1; 9330 -5.0; 10263 -2.5; 11289 -1.7; 12418 -1.7; 13660 -1.7; 15026 -2.6; 16529 -1.7; 18182 -1.7; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thermaltake Isurus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thermaltake Isurus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 159 Hz   | 0.59 | -5.0 dB |
| Peaking | 362 Hz   | 1.32 | -3.1 dB |
| Peaking | 1938 Hz  | 4.06 | -1.7 dB |
| Peaking | 6307 Hz  | 2.21 | -4.6 dB |
| Peaking | 15246 Hz | 2.58 | -0.4 dB |
| Peaking | 1007 Hz  | 3.05 | 0.9 dB  |
| Peaking | 3570 Hz  | 5.55 | 2.2 dB  |
| Peaking | 7560 Hz  | 5.76 | 1.5 dB  |
| Peaking | 9415 Hz  | 3.14 | -3.5 dB |
| Peaking | 10590 Hz | 2.94 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thermaltake%20Isurus/Thermaltake%20Isurus.png)
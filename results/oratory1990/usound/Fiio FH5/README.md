# Fiio FH5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.5; 25 -11.4; 28 -11.2; 31 -11.0; 34 -10.8; 37 -10.6; 41 -10.4; 45 -10.2; 49 -10.1; 54 -9.9; 60 -9.8; 66 -9.7; 72 -9.7; 79 -9.7; 87 -9.7; 96 -9.7; 106 -9.7; 116 -9.6; 128 -9.6; 141 -9.4; 155 -9.2; 170 -9.1; 187 -8.8; 206 -8.5; 227 -8.3; 249 -8.0; 274 -7.8; 302 -7.6; 332 -7.3; 365 -7.2; 402 -7.1; 442 -7.0; 486 -6.9; 535 -6.9; 588 -6.9; 647 -6.8; 712 -6.7; 783 -6.7; 861 -6.8; 947 -7.0; 1042 -7.5; 1146 -8.0; 1261 -8.3; 1387 -8.0; 1526 -7.6; 1678 -7.1; 1846 -6.9; 2031 -6.8; 2234 -6.5; 2457 -5.6; 2703 -4.4; 2973 -3.3; 3270 -1.8; 3597 -0.6; 3957 -0.7; 4353 -0.7; 4788 -0.5; 5267 -3.6; 5793 -3.5; 6373 -5.7; 7010 -9.0; 7711 -9.8; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -9.3; 18182 -11.6; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.59 | -4.7 dB |
| Peaking | 112 Hz   | 0.46 | -2.7 dB |
| Peaking | 4170 Hz  | 1.73 | 6.7 dB  |
| Peaking | 7408 Hz  | 5.11 | -4.9 dB |
| Peaking | 18362 Hz | 1.35 | -5.7 dB |
| Peaking | 1278 Hz  | 2.79 | -1.9 dB |
| Peaking | 2071 Hz  | 2.49 | -1.0 dB |
| Peaking | 3201 Hz  | 4.21 | 1.3 dB  |
| Peaking | 12210 Hz | 1.89 | 0.2 dB  |
| Peaking | 14313 Hz | 4.2  | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Fiio%20FH5/Fiio%20FH5.png)
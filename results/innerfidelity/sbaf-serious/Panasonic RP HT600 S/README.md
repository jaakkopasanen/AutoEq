# Panasonic RP HT600 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.7; 25 -4.8; 28 -6.0; 31 -7.0; 34 -7.7; 37 -8.1; 41 -8.5; 45 -8.7; 49 -8.8; 54 -8.8; 60 -8.8; 66 -8.7; 72 -8.7; 79 -8.8; 87 -8.8; 96 -9.0; 106 -8.9; 116 -8.6; 128 -8.9; 141 -9.3; 155 -9.5; 170 -9.3; 187 -9.4; 206 -9.6; 227 -9.6; 249 -9.7; 274 -9.9; 302 -9.9; 332 -9.9; 365 -10.0; 402 -9.9; 442 -9.8; 486 -10.0; 535 -10.1; 588 -9.6; 647 -9.2; 712 -8.8; 783 -8.0; 861 -6.8; 947 -5.1; 1042 -4.5; 1146 -4.6; 1261 -6.0; 1387 -8.6; 1526 -10.6; 1678 -11.0; 1846 -10.5; 2031 -8.0; 2234 -6.4; 2457 -4.7; 2703 -3.0; 2973 -1.4; 3270 -0.8; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.3; 9330 -11.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP HT600 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP HT600 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 3.24 | 3.9 dB   |
| Peaking | 303 Hz  | 0.26 | -4.0 dB  |
| Peaking | 1788 Hz | 1.95 | -10.2 dB |
| Peaking | 3059 Hz | 0.34 | 7.7 dB   |
| Peaking | 9127 Hz | 2.9  | -8.1 dB  |
| Peaking | 43 Hz   | 2.04 | -1.6 dB  |
| Peaking | 654 Hz  | 1.76 | -1.6 dB  |
| Peaking | 1064 Hz | 2.6  | 2.9 dB   |
| Peaking | 1461 Hz | 5.79 | -2.0 dB  |
| Peaking | 6058 Hz | 7.29 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Panasonic%20RP%20HT600%20S/Panasonic%20RP%20HT600%20S.png)
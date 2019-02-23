# Urbanears Plattan
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.5; 25 -7.0; 28 -7.6; 31 -8.1; 34 -8.4; 37 -8.7; 41 -9.0; 45 -9.2; 49 -9.3; 54 -9.5; 60 -9.6; 66 -9.8; 72 -10.0; 79 -10.2; 87 -10.2; 96 -10.2; 106 -10.3; 116 -10.4; 128 -10.1; 141 -10.5; 155 -10.8; 170 -11.2; 187 -11.4; 206 -11.4; 227 -11.1; 249 -11.1; 274 -11.0; 302 -10.6; 332 -9.9; 365 -9.5; 402 -9.6; 442 -10.6; 486 -11.4; 535 -12.2; 588 -12.7; 647 -13.3; 712 -14.0; 783 -14.5; 861 -15.0; 947 -15.2; 1042 -14.5; 1146 -12.7; 1261 -11.8; 1387 -11.0; 1526 -9.4; 1678 -7.7; 1846 -5.6; 2031 -3.7; 2234 -1.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.2; 5793 -0.5; 6373 -1.4; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Urbanears Plattan GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Urbanears Plattan ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 77 Hz   |  0.57 | -3.3 dB |
| Peaking | 206 Hz  |  1.34 | -3.0 dB |
| Peaking | 925 Hz  |  0.8  | -9.3 dB |
| Peaking | 2577 Hz |  1.21 | 7.5 dB  |
| Peaking | 4883 Hz |  1.47 | 4.6 dB  |
| Peaking | 3771 Hz |  4.8  | 0.6 dB  |
| Peaking | 5224 Hz | 12.15 | -3.4 dB |
| Peaking | 6101 Hz |  3.08 | 4.2 dB  |
| Peaking | 7147 Hz |  1.45 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -9.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Urbanears%20Plattan/Urbanears%20Plattan.png)
# Urbanears Plattan
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.7; 49 -0.9; 54 -1.0; 60 -1.2; 66 -1.3; 72 -1.5; 79 -1.7; 87 -1.8; 96 -1.8; 106 -1.9; 116 -1.9; 128 -1.7; 141 -2.0; 155 -2.4; 170 -2.7; 187 -2.9; 206 -2.9; 227 -2.7; 249 -2.7; 274 -2.5; 302 -2.1; 332 -1.5; 365 -1.0; 402 -1.1; 442 -2.1; 486 -3.0; 535 -3.7; 588 -4.2; 647 -4.8; 712 -5.5; 783 -6.1; 861 -6.6; 947 -6.8; 1042 -6.0; 1146 -4.2; 1261 -3.3; 1387 -2.5; 1526 -0.9; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Urbanears Plattan GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Urbanears Plattan ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.29 | 5.9 dB  |
| Peaking | 152 Hz  | 0.77 | 2.3 dB  |
| Peaking | 376 Hz  | 1.95 | 4.6 dB  |
| Peaking | 2072 Hz | 1.18 | 5.8 dB  |
| Peaking | 4742 Hz | 1.32 | 5.7 dB  |
| Peaking | 927 Hz  | 3.91 | -2.2 dB |
| Peaking | 1521 Hz | 5.22 | 1.5 dB  |
| Peaking | 4767 Hz | 5.84 | -1.0 dB |
| Peaking | 6410 Hz | 2.86 | 3.9 dB  |
| Peaking | 7534 Hz | 1.91 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | 3.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Urbanears%20Plattan/Urbanears%20Plattan.png)
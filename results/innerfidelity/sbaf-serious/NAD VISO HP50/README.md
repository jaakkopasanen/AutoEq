# NAD VISO HP50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.8; 25 -8.8; 28 -8.8; 31 -8.9; 34 -8.8; 37 -8.8; 41 -8.7; 45 -8.6; 49 -8.5; 54 -8.3; 60 -8.1; 66 -8.0; 72 -8.0; 79 -7.8; 87 -7.7; 96 -7.7; 106 -8.3; 116 -8.2; 128 -8.0; 141 -9.3; 155 -10.0; 170 -8.1; 187 -10.0; 206 -9.8; 227 -9.2; 249 -8.7; 274 -7.9; 302 -6.9; 332 -6.5; 365 -6.3; 402 -5.9; 442 -5.5; 486 -5.7; 535 -5.6; 588 -5.3; 647 -5.4; 712 -5.6; 783 -5.6; 861 -5.7; 947 -5.6; 1042 -5.7; 1146 -6.1; 1261 -7.1; 1387 -7.8; 1526 -8.2; 1678 -8.3; 1846 -7.6; 2031 -6.8; 2234 -5.8; 2457 -4.5; 2703 -3.5; 2973 -3.2; 3270 -3.4; 3597 -4.2; 3957 -4.9; 4353 -5.3; 4788 -6.9; 5267 -3.2; 5793 -0.7; 6373 -0.5; 7010 -2.9; 7711 -6.0; 8482 -7.1; 9330 -6.7; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.31 | -3.2 dB |
| Peaking | 193 Hz  | 1.28 | -3.8 dB |
| Peaking | 1547 Hz | 2.98 | 0.8 dB  |
| Peaking | 1605 Hz | 1.54 | -6.2 dB |
| Peaking | 2327 Hz | 0.4  | 2.9 dB  |
| Peaking | 2171 Hz | 5.16 | -0.6 dB |
| Peaking | 2828 Hz | 3.68 | 1.0 dB  |
| Peaking | 4805 Hz | 3.01 | -5.3 dB |
| Peaking | 6010 Hz | 2.14 | 6.7 dB  |
| Peaking | 8189 Hz | 2.3  | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)
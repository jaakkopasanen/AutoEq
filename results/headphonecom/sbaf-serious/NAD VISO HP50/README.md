# NAD VISO HP50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.2; 25 -10.2; 28 -10.1; 31 -10.0; 34 -9.8; 37 -9.7; 41 -9.5; 45 -9.3; 49 -9.1; 54 -9.0; 60 -8.7; 66 -8.5; 72 -8.3; 79 -8.0; 87 -7.7; 96 -7.3; 106 -7.0; 116 -7.4; 128 -9.2; 141 -10.3; 155 -9.3; 170 -8.0; 187 -9.2; 206 -9.4; 227 -9.1; 249 -8.5; 274 -7.8; 302 -7.0; 332 -5.9; 365 -6.0; 402 -5.5; 442 -5.2; 486 -5.1; 535 -4.7; 588 -4.3; 647 -4.0; 712 -3.9; 783 -4.3; 861 -4.7; 947 -4.4; 1042 -4.1; 1146 -4.4; 1261 -5.7; 1387 -6.9; 1526 -7.7; 1678 -7.5; 1846 -6.2; 2031 -5.5; 2234 -4.3; 2457 -3.0; 2703 -1.7; 2973 -1.0; 3270 -1.2; 3597 -1.8; 3957 -3.2; 4353 -5.8; 4788 -6.5; 5267 -3.2; 5793 -1.3; 6373 -0.5; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.5; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.73 | -4.6 dB |
| Peaking | 53 Hz    | 1.14 | -1.9 dB |
| Peaking | 176 Hz   | 1.26 | -4.0 dB |
| Peaking | 3067 Hz  | 3.15 | 4.9 dB  |
| Peaking | 6254 Hz  | 4.83 | 5.2 dB  |
| Peaking | 248 Hz   | 4.56 | -1.1 dB |
| Peaking | 624 Hz   | 1.8  | 1.1 dB  |
| Peaking | 1340 Hz  | 1.01 | 2.4 dB  |
| Peaking | 1537 Hz  | 2.32 | -5.1 dB |
| Peaking | 22050 Hz | 2.01 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)
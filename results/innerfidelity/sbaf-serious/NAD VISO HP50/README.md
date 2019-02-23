# NAD VISO HP50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.7; 31 -8.7; 34 -8.7; 37 -8.6; 41 -8.5; 45 -8.4; 49 -8.3; 54 -8.1; 60 -8.0; 66 -7.8; 72 -7.8; 79 -7.6; 87 -7.5; 96 -7.5; 106 -8.1; 116 -8.0; 128 -7.8; 141 -9.1; 155 -9.8; 170 -7.9; 187 -9.8; 206 -9.7; 227 -9.1; 249 -8.5; 274 -7.7; 302 -6.7; 332 -6.3; 365 -6.1; 402 -5.7; 442 -5.3; 486 -5.5; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.4; 783 -5.5; 861 -5.5; 947 -5.4; 1042 -5.5; 1146 -5.9; 1261 -6.9; 1387 -7.6; 1526 -8.0; 1678 -8.1; 1846 -7.4; 2031 -6.6; 2234 -5.6; 2457 -4.3; 2703 -3.3; 2973 -3.1; 3270 -3.2; 3597 -4.0; 3957 -4.7; 4353 -5.1; 4788 -6.7; 5267 -3.1; 5793 -0.5; 6373 -0.6; 7010 -3.5; 7711 -5.9; 8482 -6.9; 9330 -6.5; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.35 | -2.6 dB |
| Peaking | 188 Hz  | 1.82 | -3.3 dB |
| Peaking | 3120 Hz | 1.69 | 7.1 dB  |
| Peaking | 3652 Hz | 0.62 | -4.2 dB |
| Peaking | 6041 Hz | 3.2  | 8.2 dB  |
| Peaking | 243 Hz  | 3.35 | -1.0 dB |
| Peaking | 792 Hz  | 0.52 | 1.4 dB  |
| Peaking | 1585 Hz | 2.16 | -2.5 dB |
| Peaking | 2655 Hz | 2.53 | 1.0 dB  |
| Peaking | 3050 Hz | 5.47 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)
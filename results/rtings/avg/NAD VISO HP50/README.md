# NAD VISO HP50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.0; 25 -2.0; 28 -2.1; 31 -2.2; 34 -2.1; 37 -2.1; 41 -1.9; 45 -1.7; 49 -1.6; 54 -1.6; 60 -1.8; 66 -2.3; 72 -2.7; 79 -3.2; 87 -3.7; 96 -4.1; 106 -4.7; 116 -5.2; 128 -5.7; 141 -6.1; 155 -6.3; 170 -6.6; 187 -6.8; 206 -6.8; 227 -6.6; 249 -6.6; 274 -6.6; 302 -6.4; 332 -6.0; 365 -5.3; 402 -4.8; 442 -4.3; 486 -4.6; 535 -4.9; 588 -5.0; 647 -4.9; 712 -4.4; 783 -3.7; 861 -3.3; 947 -3.1; 1042 -2.8; 1146 -2.6; 1261 -2.7; 1387 -3.3; 1526 -4.0; 1678 -4.9; 1846 -5.2; 2031 -4.9; 2234 -3.3; 2457 -1.5; 2703 -0.8; 2973 -0.5; 3270 -0.7; 3597 -0.8; 3957 -1.3; 4353 -2.1; 4788 -4.0; 5267 -4.7; 5793 -3.9; 6373 -3.7; 7010 -1.5; 7711 -2.6; 8482 -2.9; 9330 -2.9; 10263 -2.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 214 Hz  | 0.88 | -4.2 dB |
| Peaking | 627 Hz  | 2.32 | -1.8 dB |
| Peaking | 1908 Hz | 1.75 | -6.8 dB |
| Peaking | 2412 Hz | 0.72 | 5.1 dB  |
| Peaking | 5205 Hz | 3    | -3.4 dB |
| Peaking | 60 Hz   | 0.62 | 2.3 dB  |
| Peaking | 114 Hz  | 0.76 | -2.0 dB |
| Peaking | 243 Hz  | 1.15 | 1.4 dB  |
| Peaking | 302 Hz  | 2.58 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)
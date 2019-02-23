# V-Moda M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.7; 25 -10.9; 28 -11.1; 31 -11.3; 34 -11.4; 37 -11.5; 41 -11.6; 45 -11.8; 49 -11.8; 54 -11.9; 60 -12.1; 66 -12.2; 72 -12.0; 79 -12.1; 87 -13.0; 96 -12.7; 106 -12.4; 116 -13.1; 128 -13.4; 141 -13.3; 155 -13.0; 170 -12.2; 187 -12.0; 206 -11.0; 227 -10.0; 249 -8.9; 274 -7.6; 302 -7.4; 332 -5.4; 365 -4.4; 402 -4.0; 442 -4.2; 486 -4.4; 535 -4.6; 588 -5.0; 647 -5.8; 712 -6.5; 783 -7.1; 861 -7.5; 947 -7.9; 1042 -8.0; 1146 -7.8; 1261 -7.6; 1387 -7.5; 1526 -7.3; 1678 -7.4; 1846 -7.1; 2031 -7.5; 2234 -7.7; 2457 -7.2; 2703 -7.2; 2973 -6.4; 3270 -5.8; 3597 -6.3; 3957 -6.3; 4353 -5.2; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.1; 9330 -11.9; 10263 -11.1; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.57 | -5.1 dB |
| Peaking | 108 Hz  | 1.4  | -4.2 dB |
| Peaking | 169 Hz  | 2.28 | -4.1 dB |
| Peaking | 5697 Hz | 2.54 | 7.2 dB  |
| Peaking | 9574 Hz | 3.98 | -6.9 dB |
| Peaking | 262 Hz  | 1.42 | -2.8 dB |
| Peaking | 392 Hz  | 1.02 | 4.3 dB  |
| Peaking | 851 Hz  | 2.02 | -0.9 dB |
| Peaking | 1083 Hz | 1.54 | -1.4 dB |
| Peaking | 2254 Hz | 1.93 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20M-100/V-Moda%20M-100.png)
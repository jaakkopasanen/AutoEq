# V-Moda M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.3; 25 -9.5; 28 -9.8; 31 -9.9; 34 -10.0; 37 -10.1; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.6; 60 -10.7; 66 -10.8; 72 -10.7; 79 -10.7; 87 -11.7; 96 -11.4; 106 -11.1; 116 -11.8; 128 -12.0; 141 -12.0; 155 -11.6; 170 -10.8; 187 -10.6; 206 -9.7; 227 -8.6; 249 -7.5; 274 -6.2; 302 -6.1; 332 -4.1; 365 -3.1; 402 -2.7; 442 -2.8; 486 -3.0; 535 -3.3; 588 -3.7; 647 -4.4; 712 -5.1; 783 -5.7; 861 -6.2; 947 -6.5; 1042 -6.7; 1146 -6.5; 1261 -6.2; 1387 -6.1; 1526 -6.0; 1678 -6.0; 1846 -5.8; 2031 -6.1; 2234 -6.3; 2457 -5.9; 2703 -5.8; 2973 -5.1; 3270 -4.5; 3597 -4.9; 3957 -4.9; 4353 -3.9; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -10.5; 10263 -9.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.37 | -3.4 dB |
| Peaking | 150 Hz  | 0.89 | -4.2 dB |
| Peaking | 414 Hz  | 1.28 | 5.1 dB  |
| Peaking | 5548 Hz | 1.86 | 6.8 dB  |
| Peaking | 9523 Hz | 3.72 | -5.5 dB |
| Peaking | 598 Hz  | 5.98 | 0.7 dB  |
| Peaking | 967 Hz  | 3.48 | -0.8 dB |
| Peaking | 3233 Hz | 5.51 | 1.3 dB  |
| Peaking | 4198 Hz | 2.51 | -1.1 dB |
| Peaking | 4745 Hz | 9.7  | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20M-100/V-Moda%20M-100.png)
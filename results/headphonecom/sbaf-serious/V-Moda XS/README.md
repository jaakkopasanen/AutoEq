# V-Moda XS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.9; 25 -11.2; 28 -11.5; 31 -11.7; 34 -11.9; 37 -12.1; 41 -12.2; 45 -12.2; 49 -12.3; 54 -12.4; 60 -12.5; 66 -12.5; 72 -12.7; 79 -12.6; 87 -12.4; 96 -12.0; 106 -12.1; 116 -12.2; 128 -12.2; 141 -12.0; 155 -11.7; 170 -11.1; 187 -10.7; 206 -10.0; 227 -10.2; 249 -9.9; 274 -8.3; 302 -7.0; 332 -5.9; 365 -5.3; 402 -4.6; 442 -4.0; 486 -3.5; 535 -3.1; 588 -2.7; 647 -2.8; 712 -2.9; 783 -3.3; 861 -4.0; 947 -4.9; 1042 -5.7; 1146 -6.2; 1261 -6.7; 1387 -6.8; 1526 -7.0; 1678 -6.9; 1846 -6.9; 2031 -7.4; 2234 -6.9; 2457 -7.5; 2703 -8.0; 2973 -8.3; 3270 -7.4; 3597 -4.8; 3957 -2.0; 4353 -1.6; 4788 -4.8; 5267 -1.6; 5793 -0.5; 6373 -2.0; 7010 -5.2; 7711 -6.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda XS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.65 | -5.3 dB |
| Peaking | 87 Hz    | 1.19 | -3.8 dB |
| Peaking | 161 Hz   | 1.8  | -3.9 dB |
| Peaking | 5594 Hz  | 2.6  | 5.8 dB  |
| Peaking | 22050 Hz | 2.63 | 2.7 dB  |
| Peaking | 243 Hz   | 4.34 | -2.7 dB |
| Peaking | 594 Hz   | 1.16 | 4.2 dB  |
| Peaking | 3008 Hz  | 0.85 | -2.4 dB |
| Peaking | 4040 Hz  | 5.11 | 5.8 dB  |
| Peaking | 8199 Hz  | 4.72 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)
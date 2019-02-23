# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.5; 25 -3.8; 28 -4.3; 31 -4.7; 34 -5.0; 37 -5.3; 41 -5.6; 45 -5.9; 49 -6.1; 54 -6.4; 60 -6.7; 66 -6.8; 72 -7.0; 79 -7.2; 87 -7.4; 96 -8.0; 106 -8.3; 116 -8.3; 128 -8.6; 141 -8.9; 155 -9.1; 170 -8.9; 187 -9.2; 206 -9.3; 227 -9.6; 249 -9.5; 274 -9.5; 302 -9.4; 332 -9.0; 365 -8.8; 402 -8.6; 442 -8.4; 486 -8.1; 535 -7.4; 588 -6.9; 647 -6.9; 712 -6.2; 783 -5.5; 861 -4.8; 947 -3.8; 1042 -2.7; 1146 -1.7; 1261 -1.8; 1387 -2.4; 1526 -3.6; 1678 -5.0; 1846 -6.7; 2031 -9.0; 2234 -8.2; 2457 -5.1; 2703 -1.1; 2973 -0.5; 3270 -0.8; 3597 -2.1; 3957 -3.8; 4353 -6.3; 4788 -5.4; 5267 -6.0; 5793 -6.5; 6373 -7.6; 7010 -10.7; 7711 -9.8; 8482 -7.9; 9330 -6.8; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.69 | 4.4 dB  |
| Peaking | 227 Hz  | 0.54 | -3.1 dB |
| Peaking | 1162 Hz | 2.38 | 5.6 dB  |
| Peaking | 3148 Hz | 3.43 | 6.8 dB  |
| Peaking | 7252 Hz | 4.38 | -4.7 dB |
| Peaking | 1508 Hz | 3.64 | 1.4 dB  |
| Peaking | 2110 Hz | 4.15 | -4.6 dB |
| Peaking | 2398 Hz | 4.15 | 0.4 dB  |
| Peaking | 2709 Hz | 9.03 | 2.8 dB  |
| Peaking | 5309 Hz | 4.44 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K712/AKG%20K712.png)
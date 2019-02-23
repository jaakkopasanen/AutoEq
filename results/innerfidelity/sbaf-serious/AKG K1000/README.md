# AKG K1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.3; 72 -2.9; 79 -4.4; 87 -5.6; 96 -6.5; 106 -6.8; 116 -6.9; 128 -6.9; 141 -6.3; 155 -6.1; 170 -5.8; 187 -5.6; 206 -5.5; 227 -5.3; 249 -5.1; 274 -4.9; 302 -4.7; 332 -4.6; 365 -4.5; 402 -4.5; 442 -4.3; 486 -4.3; 535 -4.4; 588 -4.1; 647 -4.1; 712 -4.3; 783 -4.1; 861 -4.5; 947 -4.7; 1042 -5.1; 1146 -5.7; 1261 -7.1; 1387 -8.8; 1526 -9.6; 1678 -9.8; 1846 -11.8; 2031 -11.6; 2234 -10.7; 2457 -7.9; 2703 -4.9; 2973 -2.7; 3270 -2.3; 3597 -3.9; 3957 -6.9; 4353 -7.8; 4788 -7.8; 5267 -7.8; 5793 -9.5; 6373 -10.2; 7010 -9.0; 7711 -9.2; 8482 -9.7; 9330 -8.9; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.82 | 7.1 dB  |
| Peaking | 775 Hz  | 0.57 | 3.2 dB  |
| Peaking | 1969 Hz | 1.27 | -7.5 dB |
| Peaking | 3071 Hz | 2.54 | 7.6 dB  |
| Peaking | 6687 Hz | 1.22 | -3.3 dB |
| Peaking | 37 Hz   | 3.4  | -1.2 dB |
| Peaking | 60 Hz   | 2.8  | 2.7 dB  |
| Peaking | 105 Hz  | 2    | -2.2 dB |
| Peaking | 8975 Hz | 4.33 | -2.6 dB |
| Peaking | 9958 Hz | 1.65 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K1000/AKG%20K1000.png)
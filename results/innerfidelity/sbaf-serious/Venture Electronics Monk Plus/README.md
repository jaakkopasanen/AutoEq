# Venture Electronics Monk Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.0; 106 -2.2; 116 -3.2; 128 -4.4; 141 -5.4; 155 -6.3; 170 -6.6; 187 -6.9; 206 -6.6; 227 -6.7; 249 -6.6; 274 -6.5; 302 -6.0; 332 -5.7; 365 -5.2; 402 -6.9; 442 -5.0; 486 -4.8; 535 -4.6; 588 -4.2; 647 -4.2; 712 -4.2; 783 -4.1; 861 -4.2; 947 -4.3; 1042 -4.5; 1146 -4.7; 1261 -5.3; 1387 -6.3; 1526 -8.0; 1678 -9.5; 1846 -10.8; 2031 -12.0; 2234 -12.7; 2457 -12.0; 2703 -11.0; 2973 -8.6; 3270 -5.8; 3597 -4.5; 3957 -5.1; 4353 -7.3; 4788 -8.8; 5267 -7.2; 5793 -6.5; 6373 -4.2; 7010 -8.9; 7711 -10.4; 8482 -9.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.9; 15026 -11.5; 16529 -7.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Monk Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.53 | 7.0 dB  |
| Peaking | 856 Hz   | 1.13 | 2.9 dB  |
| Peaking | 2160 Hz  | 2.27 | -7.1 dB |
| Peaking | 14949 Hz | 3.4  | -5.5 dB |
| Peaking | 22050 Hz | 1.88 | -1.9 dB |
| Peaking | 20 Hz    | 3.04 | 1.8 dB  |
| Peaking | 93 Hz    | 2.91 | 2.3 dB  |
| Peaking | 176 Hz   | 1.57 | -2.0 dB |
| Peaking | 3573 Hz  | 6.87 | 3.6 dB  |
| Peaking | 7806 Hz  | 5.98 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Venture%20Electronics%20Monk%20Plus/Venture%20Electronics%20Monk%20Plus.png)
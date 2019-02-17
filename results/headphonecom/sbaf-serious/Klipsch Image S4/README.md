# Klipsch Image S4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.5; 25 -12.5; 28 -12.6; 31 -12.6; 34 -12.7; 37 -12.7; 41 -12.8; 45 -12.9; 49 -13.1; 54 -13.3; 60 -13.6; 66 -13.7; 72 -14.0; 79 -14.1; 87 -14.3; 96 -14.4; 106 -14.4; 116 -14.5; 128 -14.4; 141 -14.4; 155 -14.3; 170 -14.1; 187 -13.8; 206 -13.4; 227 -13.0; 249 -12.5; 274 -12.0; 302 -11.3; 332 -10.6; 365 -9.8; 402 -9.0; 442 -8.4; 486 -7.8; 535 -7.2; 588 -6.4; 647 -5.6; 712 -5.0; 783 -4.5; 861 -4.1; 947 -4.2; 1042 -4.4; 1146 -4.6; 1261 -4.8; 1387 -5.4; 1526 -6.0; 1678 -6.5; 1846 -6.6; 2031 -6.8; 2234 -6.9; 2457 -6.4; 2703 -5.8; 2973 -4.4; 3270 -2.2; 3597 -0.5; 3957 -1.1; 4353 -3.2; 4788 -4.8; 5267 -6.0; 5793 -7.7; 6373 -5.4; 7010 -2.4; 7711 -4.0; 8482 -4.2; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.4; 13660 -9.6; 15026 -10.7; 16529 -5.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image S4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.3  | -7.2 dB |
| Peaking | 108 Hz   | 0.56 | -6.5 dB |
| Peaking | 243 Hz   | 0.76 | -4.8 dB |
| Peaking | 3706 Hz  | 6.75 | 4.6 dB  |
| Peaking | 14656 Hz | 3.05 | -7.7 dB |
| Peaking | 902 Hz   | 1.96 | 1.6 dB  |
| Peaking | 2318 Hz  | 1.16 | -4.1 dB |
| Peaking | 3313 Hz  | 1.31 | 2.9 dB  |
| Peaking | 5949 Hz  | 3.66 | -4.7 dB |
| Peaking | 6930 Hz  | 4.19 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4/Klipsch%20Image%20S4.png)
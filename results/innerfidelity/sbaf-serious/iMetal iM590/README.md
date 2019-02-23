# iMetal iM590
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.2; 25 -12.2; 28 -12.1; 31 -12.1; 34 -12.0; 37 -12.0; 41 -11.9; 45 -11.8; 49 -11.8; 54 -11.8; 60 -11.7; 66 -11.7; 72 -11.6; 79 -11.6; 87 -11.7; 96 -11.8; 106 -11.6; 116 -11.4; 128 -11.2; 141 -11.0; 155 -10.7; 170 -10.3; 187 -9.9; 206 -9.5; 227 -9.0; 249 -8.5; 274 -8.0; 302 -7.5; 332 -6.9; 365 -6.4; 402 -5.9; 442 -5.3; 486 -5.0; 535 -4.7; 588 -4.1; 647 -3.8; 712 -3.8; 783 -3.6; 861 -3.9; 947 -4.4; 1042 -5.0; 1146 -5.4; 1261 -5.8; 1387 -6.4; 1526 -7.3; 1678 -8.5; 1846 -9.5; 2031 -10.3; 2234 -10.7; 2457 -8.9; 2703 -6.3; 2973 -2.6; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.9; 4788 -7.9; 5267 -8.2; 5793 -7.7; 6373 -7.2; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iMetal iM590 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iMetal iM590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.35 | -5.2 dB |
| Peaking | 122 Hz  | 0.51 | -4.0 dB |
| Peaking | 704 Hz  | 0.76 | 3.5 dB  |
| Peaking | 2156 Hz | 1.67 | -5.8 dB |
| Peaking | 3381 Hz | 2.79 | 8.5 dB  |
| Peaking | 2951 Hz | 8.02 | 1.4 dB  |
| Peaking | 4098 Hz | 5.08 | 5.4 dB  |
| Peaking | 4687 Hz | 1.86 | -4.0 dB |
| Peaking | 7012 Hz | 8.6  | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iMetal%20iM590/iMetal%20iM590.png)
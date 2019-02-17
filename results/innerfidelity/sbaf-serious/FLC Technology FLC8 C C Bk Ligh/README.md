# FLC Technology FLC8 C C Bk Ligh
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -0.9; 54 -1.2; 60 -1.7; 66 -2.0; 72 -2.4; 79 -2.9; 87 -3.4; 96 -4.0; 106 -4.3; 116 -4.6; 128 -5.0; 141 -5.4; 155 -5.6; 170 -5.7; 187 -5.9; 206 -6.0; 227 -6.0; 249 -6.1; 274 -6.0; 302 -5.9; 332 -5.8; 365 -5.6; 402 -5.5; 442 -5.2; 486 -5.2; 535 -5.0; 588 -4.6; 647 -4.7; 712 -4.8; 783 -4.8; 861 -5.0; 947 -5.8; 1042 -6.9; 1146 -7.8; 1261 -8.2; 1387 -8.5; 1526 -8.0; 1678 -7.0; 1846 -5.7; 2031 -4.9; 2234 -4.6; 2457 -4.3; 2703 -4.9; 2973 -2.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.0; 7010 -7.9; 7711 -10.1; 8482 -10.4; 9330 -10.5; 10263 -10.0; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technology FLC8 C C Bk Ligh GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Bk Ligh ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.43 | 6.3 dB  |
| Peaking | 1387 Hz  | 4.02 | -2.9 dB |
| Peaking | 3694 Hz  | 1.47 | 5.4 dB  |
| Peaking | 5913 Hz  | 1.77 | 8.6 dB  |
| Peaking | 7738 Hz  | 1.46 | -8.5 dB |
| Peaking | 583 Hz   | 1.77 | 1.5 dB  |
| Peaking | 831 Hz   | 3.28 | 1.2 dB  |
| Peaking | 1135 Hz  | 4.78 | -1.2 dB |
| Peaking | 10326 Hz | 4.21 | -2.6 dB |
| Peaking | 11327 Hz | 1.73 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh.png)
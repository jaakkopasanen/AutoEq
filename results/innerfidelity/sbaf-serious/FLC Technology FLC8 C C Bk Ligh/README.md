# FLC Technology FLC8 C C Bk Ligh
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.1; 28 -1.3; 31 -1.5; 34 -1.7; 37 -1.9; 41 -2.1; 45 -2.3; 49 -2.5; 54 -2.9; 60 -3.3; 66 -3.7; 72 -4.1; 79 -4.5; 87 -5.0; 96 -5.6; 106 -6.0; 116 -6.3; 128 -6.7; 141 -7.0; 155 -7.3; 170 -7.4; 187 -7.5; 206 -7.7; 227 -7.6; 249 -7.8; 274 -7.6; 302 -7.5; 332 -7.5; 365 -7.3; 402 -7.2; 442 -6.8; 486 -6.9; 535 -6.7; 588 -6.3; 647 -6.3; 712 -6.5; 783 -6.4; 861 -6.7; 947 -7.5; 1042 -8.5; 1146 -9.5; 1261 -9.9; 1387 -10.1; 1526 -9.7; 1678 -8.7; 1846 -7.3; 2031 -6.6; 2234 -6.3; 2457 -5.9; 2703 -6.5; 2973 -4.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.1; 4788 -1.6; 5267 -0.5; 5793 -0.8; 6373 -4.6; 7010 -9.6; 7711 -11.8; 8482 -12.1; 9330 -12.2; 10263 -11.6; 11289 -8.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technology FLC8 C C Bk Ligh GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Bk Ligh ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.72 | 5.7 dB  |
| Peaking | 1356 Hz  | 2.06 | -4.0 dB |
| Peaking | 3600 Hz  | 2.88 | 6.3 dB  |
| Peaking | 5580 Hz  | 2.38 | 8.5 dB  |
| Peaking | 8214 Hz  | 1.47 | -8.0 dB |
| Peaking | 66 Hz    | 1.93 | 1.1 dB  |
| Peaking | 208 Hz   | 1.04 | -1.5 dB |
| Peaking | 10412 Hz | 4.2  | -2.6 dB |
| Peaking | 12115 Hz | 1.18 | 1.0 dB  |
| Peaking | 12213 Hz | 2.74 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh.png)
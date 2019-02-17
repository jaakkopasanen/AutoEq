# Bowers & Wilkins P5 Test 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.7; 25 -4.8; 28 -5.0; 31 -5.1; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.6; 49 -5.8; 54 -6.1; 60 -6.4; 66 -6.8; 72 -7.1; 79 -7.3; 87 -7.8; 96 -8.1; 106 -8.4; 116 -8.6; 128 -8.8; 141 -9.0; 155 -9.3; 170 -9.0; 187 -9.0; 206 -8.6; 227 -8.0; 249 -7.3; 274 -6.4; 302 -6.4; 332 -6.3; 365 -5.4; 402 -4.5; 442 -3.6; 486 -3.4; 535 -3.2; 588 -2.8; 647 -3.0; 712 -3.1; 783 -2.9; 861 -3.0; 947 -2.9; 1042 -2.9; 1146 -2.9; 1261 -3.1; 1387 -3.6; 1526 -4.3; 1678 -4.9; 1846 -5.4; 2031 -5.6; 2234 -6.5; 2457 -6.8; 2703 -6.2; 2973 -5.7; 3270 -4.7; 3597 -3.9; 3957 -2.6; 4353 -2.5; 4788 -2.5; 5267 -3.5; 5793 -5.2; 6373 -2.3; 7010 -0.5; 7711 -2.6; 8482 -2.9; 9330 -2.9; 10263 -2.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -2.9; 18182 -3.3; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Test 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Test 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.42 | -1.4 dB |
| Peaking | 103 Hz  | 0.64 | -2.8 dB |
| Peaking | 194 Hz  | 0.71 | -4.8 dB |
| Peaking | 1160 Hz | 0.16 | 1.3 dB  |
| Peaking | 2341 Hz | 1.26 | -5.0 dB |
| Peaking | 344 Hz  | 6.21 | -0.9 dB |
| Peaking | 453 Hz  | 3.73 | 0.5 dB  |
| Peaking | 4770 Hz | 2.4  | 2.8 dB  |
| Peaking | 5853 Hz | 2.14 | -4.9 dB |
| Peaking | 6805 Hz | 5.25 | 5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Test%202/Bowers%20&%20Wilkins%20P5%20Test%202.png)
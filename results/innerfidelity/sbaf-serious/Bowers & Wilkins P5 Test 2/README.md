# Bowers & Wilkins P5 Test 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.0; 25 -3.1; 28 -3.3; 31 -3.4; 34 -3.5; 37 -3.6; 41 -3.7; 45 -3.9; 49 -4.1; 54 -4.4; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.6; 87 -6.1; 96 -6.4; 106 -6.7; 116 -7.0; 128 -7.1; 141 -7.3; 155 -7.6; 170 -7.3; 187 -7.3; 206 -6.9; 227 -6.3; 249 -5.6; 274 -4.7; 302 -4.7; 332 -4.6; 365 -3.7; 402 -2.8; 442 -1.9; 486 -1.7; 535 -1.5; 588 -1.1; 647 -1.3; 712 -1.4; 783 -1.2; 861 -1.3; 947 -1.2; 1042 -1.2; 1146 -1.2; 1261 -1.4; 1387 -1.9; 1526 -2.6; 1678 -3.2; 1846 -3.7; 2031 -3.9; 2234 -4.8; 2457 -5.1; 2703 -4.5; 2973 -4.0; 3270 -3.0; 3597 -2.2; 3957 -0.9; 4353 -0.8; 4788 -0.8; 5267 -1.8; 5793 -3.5; 6373 -0.6; 7010 -0.5; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Test 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Test 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 170 Hz  | 0.56 | -5.4 dB |
| Peaking | 611 Hz  | 0.42 | 3.1 dB  |
| Peaking | 2385 Hz | 1.53 | -3.0 dB |
| Peaking | 4242 Hz | 2.82 | 2.8 dB  |
| Peaking | 6754 Hz | 9.44 | 3.8 dB  |
| Peaking | 344 Hz  | 7.02 | -0.7 dB |
| Peaking | 447 Hz  | 5.63 | 0.5 dB  |
| Peaking | 8023 Hz | 1.23 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Test%202/Bowers%20&%20Wilkins%20P5%20Test%202.png)
# Fostex T50RP 2011 A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.8; 116 -1.5; 128 -2.4; 141 -3.1; 155 -3.5; 170 -3.9; 187 -4.4; 206 -4.7; 227 -4.9; 249 -5.1; 274 -4.9; 302 -4.7; 332 -4.3; 365 -4.4; 402 -4.6; 442 -4.7; 486 -5.0; 535 -4.8; 588 -4.4; 647 -4.9; 712 -5.1; 783 -4.9; 861 -5.6; 947 -6.3; 1042 -6.1; 1146 -5.9; 1261 -5.8; 1387 -6.2; 1526 -6.9; 1678 -7.2; 1846 -6.0; 2031 -4.3; 2234 -2.8; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP 2011 A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP 2011 A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.33 | 5.9 dB  |
| Peaking | 97 Hz   | 1.23 | 3.0 dB  |
| Peaking | 431 Hz  | 1.26 | 1.6 dB  |
| Peaking | 4384 Hz | 0.78 | 7.1 dB  |
| Peaking | 8626 Hz | 1.93 | -2.9 dB |
| Peaking | 1568 Hz | 4.04 | -1.1 dB |
| Peaking | 1765 Hz | 2.74 | -1.9 dB |
| Peaking | 2576 Hz | 2.26 | 3.0 dB  |
| Peaking | 4710 Hz | 0.84 | -1.4 dB |
| Peaking | 6116 Hz | 4.03 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 3.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%202011%20A/Fostex%20T50RP%202011%20A.png)
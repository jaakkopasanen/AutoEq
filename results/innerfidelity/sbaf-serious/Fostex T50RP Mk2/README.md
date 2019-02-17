# Fostex T50RP Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.3; 34 -1.9; 37 -2.3; 41 -2.7; 45 -3.0; 49 -3.2; 54 -3.3; 60 -3.4; 66 -3.5; 72 -3.7; 79 -3.8; 87 -4.0; 96 -4.2; 106 -4.4; 116 -4.7; 128 -5.4; 141 -5.8; 155 -5.9; 170 -5.7; 187 -6.2; 206 -6.3; 227 -6.2; 249 -6.1; 274 -6.0; 302 -5.9; 332 -5.7; 365 -5.5; 402 -5.5; 442 -5.4; 486 -5.7; 535 -5.7; 588 -6.3; 647 -5.6; 712 -3.3; 783 -4.0; 861 -4.9; 947 -5.9; 1042 -7.2; 1146 -8.0; 1261 -8.0; 1387 -7.6; 1526 -7.1; 1678 -7.7; 1846 -6.5; 2031 -3.5; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.75 | 5.9 dB  |
| Peaking | 78 Hz   | 0.98 | 1.8 dB  |
| Peaking | 753 Hz  | 3.74 | 3.1 dB  |
| Peaking | 1498 Hz | 1.28 | -5.4 dB |
| Peaking | 3086 Hz | 0.64 | 7.8 dB  |
| Peaking | 1835 Hz | 5.25 | -3.0 dB |
| Peaking | 2118 Hz | 1.87 | 2.3 dB  |
| Peaking | 3169 Hz | 1.99 | -1.5 dB |
| Peaking | 6266 Hz | 2.01 | 5.9 dB  |
| Peaking | 7365 Hz | 1.41 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%20Mk2/Fostex%20T50RP%20Mk2.png)
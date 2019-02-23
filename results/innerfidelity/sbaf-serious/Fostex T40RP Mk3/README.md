# Fostex T40RP Mk3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.8; 49 -2.6; 54 -3.5; 60 -4.4; 66 -5.2; 72 -5.8; 79 -6.3; 87 -6.7; 96 -7.0; 106 -7.1; 116 -7.2; 128 -7.4; 141 -7.4; 155 -7.4; 170 -7.0; 187 -6.8; 206 -6.5; 227 -6.4; 249 -6.4; 274 -6.5; 302 -7.0; 332 -7.1; 365 -6.6; 402 -6.6; 442 -5.6; 486 -7.2; 535 -7.7; 588 -7.9; 647 -7.8; 712 -8.3; 783 -8.2; 861 -7.6; 947 -7.5; 1042 -6.9; 1146 -6.8; 1261 -5.9; 1387 -5.9; 1526 -5.8; 1678 -6.0; 1846 -6.5; 2031 -5.8; 2234 -5.7; 2457 -5.6; 2703 -5.3; 2973 -5.6; 3270 -6.3; 3597 -7.1; 3957 -8.6; 4353 -9.4; 4788 -8.1; 5267 -3.4; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -11.0; 10263 -8.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T40RP Mk3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T40RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 29 Hz    |  1.12 | 7.0 dB   |
| Peaking | 717 Hz   |  1.79 | -1.9 dB  |
| Peaking | 4533 Hz  |  1.91 | -13.5 dB |
| Peaking | 5477 Hz  |  1.08 | 13.6 dB  |
| Peaking | 9069 Hz  |  2.13 | -7.7 dB  |
| Peaking | 46 Hz    |  2.78 | 1.4 dB   |
| Peaking | 119 Hz   |  0.99 | -1.4 dB  |
| Peaking | 222 Hz   |  2.75 | 0.6 dB   |
| Peaking | 7323 Hz  | 11.99 | -1.6 dB  |
| Peaking | 10954 Hz |  9.68 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T40RP%20Mk3/Fostex%20T40RP%20Mk3.png)
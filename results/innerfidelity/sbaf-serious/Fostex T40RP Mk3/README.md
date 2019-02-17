# Fostex T40RP Mk3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.2; 49 -2.0; 54 -2.9; 60 -3.8; 66 -4.5; 72 -5.1; 79 -5.7; 87 -6.1; 96 -6.4; 106 -6.5; 116 -6.6; 128 -6.8; 141 -6.8; 155 -6.7; 170 -6.4; 187 -6.2; 206 -5.9; 227 -5.8; 249 -5.8; 274 -5.9; 302 -6.3; 332 -6.5; 365 -5.9; 402 -6.0; 442 -5.0; 486 -6.5; 535 -7.1; 588 -7.3; 647 -7.2; 712 -7.7; 783 -7.6; 861 -7.0; 947 -6.9; 1042 -6.3; 1146 -6.2; 1261 -5.2; 1387 -5.3; 1526 -5.2; 1678 -5.4; 1846 -5.9; 2031 -5.2; 2234 -5.0; 2457 -5.0; 2703 -4.7; 2973 -5.0; 3270 -5.7; 3597 -6.5; 3957 -8.0; 4353 -8.8; 4788 -7.5; 5267 -2.8; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -10.4; 10263 -8.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T40RP Mk3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T40RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.94 | 6.9 dB  |
| Peaking | 2693 Hz | 1.12 | 1.9 dB  |
| Peaking | 4447 Hz | 2.67 | -5.6 dB |
| Peaking | 5823 Hz | 2.54 | 7.8 dB  |
| Peaking | 9302 Hz | 4.09 | -4.9 dB |
| Peaking | 48 Hz   | 3.02 | 1.2 dB  |
| Peaking | 118 Hz  | 1.01 | -1.3 dB |
| Peaking | 287 Hz  | 0.48 | 0.9 dB  |
| Peaking | 708 Hz  | 1.67 | -1.7 dB |
| Peaking | 1347 Hz | 4.16 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T40RP%20Mk3/Fostex%20T40RP%20Mk3.png)
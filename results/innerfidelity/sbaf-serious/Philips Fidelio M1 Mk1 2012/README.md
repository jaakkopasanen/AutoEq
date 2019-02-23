# Philips Fidelio M1 Mk1 2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.3; 25 -8.5; 28 -8.6; 31 -8.7; 34 -8.7; 37 -8.7; 41 -8.7; 45 -8.7; 49 -8.7; 54 -8.6; 60 -8.5; 66 -8.4; 72 -8.4; 79 -8.6; 87 -8.8; 96 -8.9; 106 -8.7; 116 -8.4; 128 -8.2; 141 -8.1; 155 -7.8; 170 -7.0; 187 -6.7; 206 -6.5; 227 -6.3; 249 -6.2; 274 -6.0; 302 -5.8; 332 -6.0; 365 -6.6; 402 -7.1; 442 -7.9; 486 -8.6; 535 -8.9; 588 -8.8; 647 -9.0; 712 -9.0; 783 -8.7; 861 -8.7; 947 -8.6; 1042 -8.5; 1146 -8.2; 1261 -8.0; 1387 -8.1; 1526 -8.2; 1678 -8.1; 1846 -7.6; 2031 -6.7; 2234 -5.8; 2457 -4.6; 2703 -3.7; 2973 -2.8; 3270 -2.2; 3597 -1.6; 3957 -1.0; 4353 -1.1; 4788 -0.5; 5267 -1.3; 5793 -1.7; 6373 -1.5; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio M1 Mk1 2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 Mk1 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.37 | -3.5 dB |
| Peaking | 646 Hz  | 1.38 | -3.2 dB |
| Peaking | 1516 Hz | 1.09 | -3.1 dB |
| Peaking | 4261 Hz | 1.05 | 5.4 dB  |
| Peaking | 129 Hz  | 1.91 | -0.8 dB |
| Peaking | 295 Hz  | 1.01 | 0.9 dB  |
| Peaking | 469 Hz  | 3.67 | -1.2 dB |
| Peaking | 6591 Hz | 3.85 | 3.0 dB  |
| Peaking | 7620 Hz | 1.76 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1%20Mk1%202012/Philips%20Fidelio%20M1%20Mk1%202012.png)
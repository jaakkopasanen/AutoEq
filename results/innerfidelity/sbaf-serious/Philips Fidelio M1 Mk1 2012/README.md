# Philips Fidelio M1 Mk1 2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.4; 28 -6.5; 31 -6.6; 34 -6.6; 37 -6.6; 41 -6.6; 45 -6.6; 49 -6.6; 54 -6.5; 60 -6.4; 66 -6.3; 72 -6.3; 79 -6.5; 87 -6.7; 96 -6.8; 106 -6.6; 116 -6.3; 128 -6.1; 141 -6.0; 155 -5.7; 170 -4.9; 187 -4.6; 206 -4.4; 227 -4.2; 249 -4.1; 274 -3.9; 302 -3.7; 332 -3.9; 365 -4.5; 402 -5.0; 442 -5.8; 486 -6.5; 535 -6.8; 588 -6.7; 647 -6.9; 712 -6.9; 783 -6.6; 861 -6.6; 947 -6.5; 1042 -6.4; 1146 -6.1; 1261 -5.9; 1387 -6.0; 1526 -6.1; 1678 -6.0; 1846 -5.5; 2031 -4.6; 2234 -3.7; 2457 -2.5; 2703 -1.6; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio M1 Mk1 2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 Mk1 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 279 Hz  | 0.85 | 5.6 dB  |
| Peaking | 334 Hz  | 0.44 | -2.8 dB |
| Peaking | 3354 Hz | 1.3  | 6.1 dB  |
| Peaking | 5621 Hz | 2.69 | 4.7 dB  |
| Peaking | 1708 Hz | 2.57 | -1.8 dB |
| Peaking | 1754 Hz | 1.26 | 1.2 dB  |
| Peaking | 6399 Hz | 7.24 | 1.7 dB  |
| Peaking | 6677 Hz | 5.78 | 0.9 dB  |
| Peaking | 7711 Hz | 1.99 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1%20Mk1%202012/Philips%20Fidelio%20M1%20Mk1%202012.png)
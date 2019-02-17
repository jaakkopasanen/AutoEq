# Philips Fidelio S1 Early 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.6; 28 -5.6; 31 -5.6; 34 -5.6; 37 -5.6; 41 -5.6; 45 -5.7; 49 -5.7; 54 -5.8; 60 -6.0; 66 -6.1; 72 -6.3; 79 -6.5; 87 -6.7; 96 -6.9; 106 -6.9; 116 -6.9; 128 -7.0; 141 -6.9; 155 -6.9; 170 -6.7; 187 -6.6; 206 -6.4; 227 -6.0; 249 -5.8; 274 -5.5; 302 -5.2; 332 -4.9; 365 -4.7; 402 -4.4; 442 -4.1; 486 -3.2; 535 -3.6; 588 -3.2; 647 -3.0; 712 -3.1; 783 -3.0; 861 -3.4; 947 -3.8; 1042 -4.3; 1146 -4.8; 1261 -5.4; 1387 -6.1; 1526 -6.9; 1678 -7.4; 1846 -7.5; 2031 -7.3; 2234 -6.9; 2457 -5.8; 2703 -4.6; 2973 -3.2; 3270 -2.1; 3597 -2.1; 3957 -3.9; 4353 -7.3; 4788 -8.9; 5267 -6.8; 5793 -3.1; 6373 -0.5; 7010 -1.6; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio S1 Early 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S1 Early 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 107 Hz  | 0.6  | -3.0 dB |
| Peaking | 1889 Hz | 2.05 | -3.9 dB |
| Peaking | 3516 Hz | 2.8  | 4.0 dB  |
| Peaking | 4727 Hz | 3.21 | -6.2 dB |
| Peaking | 6432 Hz | 4.53 | 5.1 dB  |
| Peaking | 25 Hz   | 1.53 | -1.1 dB |
| Peaking | 237 Hz  | 1.59 | -0.6 dB |
| Peaking | 701 Hz  | 1.1  | 1.7 dB  |
| Peaking | 1215 Hz | 2.09 | -0.6 dB |
| Peaking | 1480 Hz | 5.67 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S1%20Early%202013/Philips%20Fidelio%20S1%20Early%202013.png)
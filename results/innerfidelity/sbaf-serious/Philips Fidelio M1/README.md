# Philips Fidelio M1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.4; 25 -3.8; 28 -4.3; 31 -4.7; 34 -5.1; 37 -5.4; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.7; 60 -7.0; 66 -7.5; 72 -7.9; 79 -8.3; 87 -8.7; 96 -9.1; 106 -9.2; 116 -9.3; 128 -9.8; 141 -10.3; 155 -10.7; 170 -10.3; 187 -10.2; 206 -9.8; 227 -8.9; 249 -8.0; 274 -7.1; 302 -6.3; 332 -5.6; 365 -4.8; 402 -4.3; 442 -3.9; 486 -3.9; 535 -4.0; 588 -4.2; 647 -4.7; 712 -5.5; 783 -5.7; 861 -6.1; 947 -6.5; 1042 -6.4; 1146 -5.7; 1261 -4.7; 1387 -4.4; 1526 -5.2; 1678 -4.8; 1846 -4.4; 2031 -4.3; 2234 -3.9; 2457 -3.4; 2703 -4.9; 2973 -5.0; 3270 -5.1; 3597 -5.5; 3957 -5.6; 4353 -5.8; 4788 -4.9; 5267 -1.8; 5793 -0.5; 6373 -2.5; 7010 -4.3; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.4; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio M1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.83 | 3.7 dB  |
| Peaking | 163 Hz   | 0.71 | -4.6 dB |
| Peaking | 424 Hz   | 1.14 | 3.9 dB  |
| Peaking | 2169 Hz  | 1.51 | 2.5 dB  |
| Peaking | 5789 Hz  | 4.06 | 6.3 dB  |
| Peaking | 988 Hz   | 3.8  | -1.1 dB |
| Peaking | 1355 Hz  | 4.14 | 1.9 dB  |
| Peaking | 1504 Hz  | 4.12 | -0.9 dB |
| Peaking | 4345 Hz  | 7.9  | -0.7 dB |
| Peaking | 18787 Hz | 1.69 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1/Philips%20Fidelio%20M1.png)
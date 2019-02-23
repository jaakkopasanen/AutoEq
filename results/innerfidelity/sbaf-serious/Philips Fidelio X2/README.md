# Philips Fidelio X2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -2.2; 25 -3.0; 28 -4.2; 31 -5.2; 34 -6.1; 37 -6.9; 41 -7.8; 45 -8.5; 49 -9.1; 54 -9.6; 60 -10.0; 66 -10.2; 72 -10.3; 79 -10.4; 87 -10.4; 96 -10.2; 106 -9.8; 116 -9.3; 128 -8.9; 141 -8.7; 155 -8.6; 170 -8.0; 187 -7.8; 206 -8.3; 227 -9.2; 249 -8.5; 274 -8.0; 302 -7.7; 332 -7.6; 365 -7.4; 402 -7.4; 442 -7.2; 486 -7.5; 535 -7.5; 588 -7.3; 647 -7.4; 712 -7.4; 783 -7.0; 861 -6.6; 947 -5.6; 1042 -4.9; 1146 -4.0; 1261 -4.1; 1387 -5.5; 1526 -7.5; 1678 -7.9; 1846 -7.4; 2031 -6.7; 2234 -6.8; 2457 -6.1; 2703 -3.3; 2973 -1.7; 3270 -3.7; 3597 -4.2; 3957 -5.3; 4353 -8.1; 4788 -9.0; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -10.5; 9330 -11.8; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.88 | 8.4 dB  |
| Peaking | 52 Hz   | 0.34 | -4.9 dB |
| Peaking | 2937 Hz | 5.81 | 5.3 dB  |
| Peaking | 6090 Hz | 4.24 | 7.1 dB  |
| Peaking | 9013 Hz | 5.19 | -6.7 dB |
| Peaking | 716 Hz  | 1.05 | -1.1 dB |
| Peaking | 1238 Hz | 2.03 | 5.2 dB  |
| Peaking | 1545 Hz | 1.8  | -3.7 dB |
| Peaking | 4607 Hz | 1.93 | 3.5 dB  |
| Peaking | 4632 Hz | 5.59 | -8.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X2/Philips%20Fidelio%20X2.png)
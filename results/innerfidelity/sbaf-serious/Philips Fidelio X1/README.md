# Philips Fidelio X1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.6; 28 -2.8; 31 -4.0; 34 -5.1; 37 -6.1; 41 -7.2; 45 -8.2; 49 -9.1; 54 -10.0; 60 -10.5; 66 -10.8; 72 -10.9; 79 -10.9; 87 -10.8; 96 -10.9; 106 -10.4; 116 -10.0; 128 -9.8; 141 -9.6; 155 -9.3; 170 -8.8; 187 -9.6; 206 -9.2; 227 -8.5; 249 -8.0; 274 -7.6; 302 -7.3; 332 -6.9; 365 -6.5; 402 -6.2; 442 -5.9; 486 -5.9; 535 -5.6; 588 -5.3; 647 -5.2; 712 -5.1; 783 -4.8; 861 -4.3; 947 -3.6; 1042 -3.4; 1146 -3.1; 1261 -3.0; 1387 -4.7; 1526 -6.1; 1678 -6.7; 1846 -6.4; 2031 -6.6; 2234 -6.3; 2457 -6.1; 2703 -4.2; 2973 -2.3; 3270 -4.1; 3597 -5.2; 3957 -5.3; 4353 -6.4; 4788 -6.7; 5267 -6.3; 5793 -7.2; 6373 -5.7; 7010 -5.2; 7711 -7.1; 8482 -9.8; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.99 | 7.0 dB  |
| Peaking | 71 Hz   | 0.68 | -5.3 dB |
| Peaking | 195 Hz  | 3.07 | -1.6 dB |
| Peaking | 1025 Hz | 1.67 | 3.5 dB  |
| Peaking | 2981 Hz | 5.62 | 4.2 dB  |
| Peaking | 551 Hz  | 1.86 | 0.8 dB  |
| Peaking | 1265 Hz | 3.82 | 3.7 dB  |
| Peaking | 1335 Hz | 1.65 | -2.6 dB |
| Peaking | 6870 Hz | 7.56 | 2.1 dB  |
| Peaking | 8786 Hz | 5.33 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X1/Philips%20Fidelio%20X1.png)
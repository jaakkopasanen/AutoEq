# Philips Fidelio S1 Early 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.6; 28 -5.6; 31 -5.6; 34 -5.6; 37 -5.6; 41 -5.6; 45 -5.7; 49 -5.7; 54 -5.8; 60 -6.0; 66 -6.1; 72 -6.3; 79 -6.5; 87 -6.7; 96 -6.9; 106 -6.9; 116 -6.9; 128 -7.0; 141 -6.9; 155 -6.9; 170 -6.7; 187 -6.6; 206 -6.4; 227 -6.0; 249 -5.8; 274 -5.5; 302 -5.2; 332 -4.9; 365 -4.7; 402 -4.4; 442 -4.1; 486 -3.2; 535 -3.6; 588 -3.2; 647 -3.0; 712 -3.1; 783 -3.0; 861 -3.4; 947 -3.8; 1042 -4.3; 1146 -4.8; 1261 -5.4; 1387 -6.1; 1526 -6.9; 1678 -7.4; 1846 -7.5; 2031 -7.3; 2234 -6.9; 2457 -5.8; 2703 -4.6; 2973 -3.2; 3270 -2.1; 3597 -2.1; 3957 -3.9; 4353 -7.3; 4788 -8.9; 5267 -6.8; 5793 -3.1; 6373 -0.5; 7010 -2.1; 7711 -4.3; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio S1 Early 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S1 Early 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 111 Hz  | 0.78 | -2.6 dB |
| Peaking | 1904 Hz | 2.34 | -3.5 dB |
| Peaking | 3520 Hz | 2.67 | 4.2 dB  |
| Peaking | 4722 Hz | 3.28 | -5.9 dB |
| Peaking | 6401 Hz | 4.62 | 5.4 dB  |
| Peaking | 26 Hz   | 1.2  | -0.8 dB |
| Peaking | 232 Hz  | 1.72 | -0.7 dB |
| Peaking | 707 Hz  | 1.01 | 2.1 dB  |
| Peaking | 1266 Hz | 1.53 | -0.7 dB |
| Peaking | 1494 Hz | 5.7  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S1%20Early%202013/Philips%20Fidelio%20S1%20Early%202013.png)
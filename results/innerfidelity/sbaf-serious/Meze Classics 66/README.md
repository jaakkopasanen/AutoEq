# Meze Classics 66
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -11.0; 25 -11.4; 28 -11.8; 31 -12.2; 34 -12.5; 37 -12.7; 41 -12.8; 45 -12.9; 49 -13.0; 54 -13.0; 60 -13.1; 66 -13.3; 72 -13.4; 79 -13.8; 87 -14.0; 96 -14.2; 106 -14.2; 116 -14.4; 128 -14.8; 141 -14.8; 155 -15.2; 170 -14.8; 187 -15.3; 206 -15.6; 227 -15.4; 249 -14.5; 274 -13.3; 302 -13.5; 332 -13.8; 365 -13.6; 402 -12.8; 442 -10.8; 486 -9.2; 535 -7.1; 588 -5.1; 647 -4.6; 712 -5.6; 783 -6.7; 861 -7.9; 947 -7.8; 1042 -6.2; 1146 -4.1; 1261 -2.0; 1387 -1.3; 1526 -1.8; 1678 -1.3; 1846 -1.3; 2031 -1.7; 2234 -1.7; 2457 -2.0; 2703 -4.3; 2973 -3.8; 3270 -0.8; 3597 -3.3; 3957 -3.0; 4353 -0.6; 4788 -0.8; 5267 -1.4; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Classics 66 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classics 66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.32 | -6.6 dB |
| Peaking | 203 Hz  | 1.04 | -5.8 dB |
| Peaking | 367 Hz  | 3.37 | -4.3 dB |
| Peaking | 1749 Hz | 1.17 | 5.3 dB  |
| Peaking | 5114 Hz | 1.61 | 5.7 dB  |
| Peaking | 633 Hz  | 4.06 | 3.5 dB  |
| Peaking | 933 Hz  | 2.43 | -2.9 dB |
| Peaking | 1268 Hz | 4.76 | 2.4 dB  |
| Peaking | 6441 Hz | 5.14 | 3.4 dB  |
| Peaking | 7553 Hz | 1.77 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -8.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classics%2066/Meze%20Classics%2066.png)
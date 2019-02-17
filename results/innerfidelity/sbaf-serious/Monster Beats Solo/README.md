# Monster Beats Solo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.8; 25 -6.2; 28 -6.7; 31 -7.1; 34 -7.4; 37 -7.8; 41 -8.2; 45 -8.3; 49 -8.2; 54 -8.3; 60 -8.7; 66 -9.1; 72 -9.7; 79 -10.5; 87 -11.2; 96 -12.2; 106 -13.1; 116 -13.4; 128 -13.3; 141 -13.6; 155 -14.1; 170 -13.9; 187 -14.0; 206 -13.2; 227 -12.7; 249 -12.5; 274 -11.7; 302 -9.8; 332 -7.8; 365 -5.9; 402 -4.8; 442 -3.5; 486 -2.8; 535 -2.9; 588 -3.6; 647 -4.7; 712 -5.7; 783 -6.2; 861 -6.5; 947 -6.6; 1042 -6.2; 1146 -5.7; 1261 -5.2; 1387 -5.1; 1526 -4.8; 1678 -4.4; 1846 -3.8; 2031 -2.9; 2234 -2.5; 2457 -1.6; 2703 -1.4; 2973 -0.8; 3270 -0.8; 3597 -0.8; 3957 -1.7; 4353 -3.8; 4788 -3.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 2.09 | -1.7 dB |
| Peaking | 204 Hz  | 0.53 | -8.2 dB |
| Peaking | 454 Hz  | 1.39 | 7.9 dB  |
| Peaking | 2936 Hz | 1.16 | 5.8 dB  |
| Peaking | 5847 Hz | 3.65 | 5.4 dB  |
| Peaking | 18 Hz   | 2.17 | 1.7 dB  |
| Peaking | 583 Hz  | 5.89 | 0.9 dB  |
| Peaking | 944 Hz  | 1.8  | -1.4 dB |
| Peaking | 1179 Hz | 1.61 | 1.0 dB  |
| Peaking | 8369 Hz | 3.85 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo/Monster%20Beats%20Solo.png)
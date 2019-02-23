# Monster Lady Gaga
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.0; 25 -9.2; 28 -9.4; 31 -9.5; 34 -9.5; 37 -9.5; 41 -9.4; 45 -9.3; 49 -9.3; 54 -9.3; 60 -9.2; 66 -9.2; 72 -9.2; 79 -9.2; 87 -9.1; 96 -9.2; 106 -8.9; 116 -8.8; 128 -8.7; 141 -8.5; 155 -8.3; 170 -8.0; 187 -7.6; 206 -7.3; 227 -6.9; 249 -6.6; 274 -6.1; 302 -5.7; 332 -5.4; 365 -5.0; 402 -4.7; 442 -4.2; 486 -4.2; 535 -3.9; 588 -3.3; 647 -3.2; 712 -3.2; 783 -3.1; 861 -3.4; 947 -3.8; 1042 -4.3; 1146 -4.7; 1261 -5.2; 1387 -6.0; 1526 -6.9; 1678 -7.5; 1846 -7.7; 2031 -7.7; 2234 -7.7; 2457 -7.2; 2703 -6.5; 2973 -4.7; 3270 -2.8; 3597 -2.2; 3957 -3.0; 4353 -5.1; 4788 -5.4; 5267 -3.6; 5793 -1.6; 6373 -0.5; 7010 -2.7; 7711 -4.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Lady Gaga GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Lady Gaga ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.19 | -4.3 dB |
| Peaking | 853 Hz   | 0.56 | 4.8 dB  |
| Peaking | 2147 Hz  | 0.49 | -5.5 dB |
| Peaking | 3465 Hz  | 2.48 | 6.5 dB  |
| Peaking | 6243 Hz  | 3.34 | 6.1 dB  |
| Peaking | 506 Hz   | 9.41 | -0.3 dB |
| Peaking | 2479 Hz  | 6.85 | 0.2 dB  |
| Peaking | 7720 Hz  | 8.71 | -0.6 dB |
| Peaking | 11337 Hz | 1.14 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Lady%20Gaga/Monster%20Lady%20Gaga.png)
# Monster Lady Gaga with control talk
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.8; 25 -12.1; 28 -12.6; 31 -12.9; 34 -13.2; 37 -13.4; 41 -13.6; 45 -13.9; 49 -14.1; 54 -14.2; 60 -14.3; 66 -14.5; 72 -14.6; 79 -14.7; 87 -14.7; 96 -14.6; 106 -14.5; 116 -14.4; 128 -14.2; 141 -14.0; 155 -13.7; 170 -13.4; 187 -12.9; 206 -12.5; 227 -12.0; 249 -11.4; 274 -10.9; 302 -10.3; 332 -9.7; 365 -9.0; 402 -8.5; 442 -8.0; 486 -7.5; 535 -7.0; 588 -6.5; 647 -6.0; 712 -5.9; 783 -5.2; 861 -5.1; 947 -5.2; 1042 -5.3; 1146 -4.7; 1261 -5.1; 1387 -5.6; 1526 -6.3; 1678 -6.9; 1846 -6.9; 2031 -6.5; 2234 -5.8; 2457 -4.9; 2703 -3.8; 2973 -2.7; 3270 -1.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Lady Gaga with control talk GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Lady Gaga with control talk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.45 | -3.6 dB |
| Peaking | 119 Hz  | 0.35 | -7.2 dB |
| Peaking | 1205 Hz | 0.38 | 2.9 dB  |
| Peaking | 1836 Hz | 1.71 | -3.7 dB |
| Peaking | 4504 Hz | 1.18 | 5.9 dB  |
| Peaking | 2571 Hz | 3.28 | -0.5 dB |
| Peaking | 3508 Hz | 2.07 | 1.3 dB  |
| Peaking | 4359 Hz | 4.33 | -1.8 dB |
| Peaking | 6333 Hz | 3.01 | 4.3 dB  |
| Peaking | 7437 Hz | 1.58 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Lady%20Gaga%20with%20control%20talk/Monster%20Lady%20Gaga%20with%20control%20talk.png)
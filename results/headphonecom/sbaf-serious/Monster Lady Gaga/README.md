# Monster Lady Gaga
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -13.1; 25 -13.4; 28 -13.8; 31 -14.2; 34 -14.5; 37 -14.7; 41 -14.9; 45 -15.1; 49 -15.4; 54 -15.5; 60 -15.6; 66 -15.8; 72 -15.9; 79 -16.0; 87 -16.0; 96 -15.9; 106 -15.8; 116 -15.6; 128 -15.5; 141 -15.2; 155 -15.0; 170 -14.6; 187 -14.2; 206 -13.8; 227 -13.2; 249 -12.7; 274 -12.2; 302 -11.6; 332 -11.0; 365 -10.3; 402 -9.8; 442 -9.3; 486 -8.8; 535 -8.3; 588 -7.8; 647 -7.3; 712 -7.2; 783 -6.5; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.0; 1261 -6.4; 1387 -6.9; 1526 -7.6; 1678 -8.2; 1846 -8.2; 2031 -7.8; 2234 -7.1; 2457 -6.2; 2703 -5.1; 2973 -4.0; 3270 -2.7; 3597 -1.7; 3957 -1.7; 4353 -2.3; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Lady Gaga GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Lady Gaga ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.31 | -8.1 dB |
| Peaking | 178 Hz  | 0.6  | -4.3 dB |
| Peaking | 3620 Hz | 3.38 | 3.9 dB  |
| Peaking | 5765 Hz | 1.89 | 6.7 dB  |
| Peaking | 8131 Hz | 2.67 | -2.6 dB |
| Peaking | 1107 Hz | 1.13 | 1.2 dB  |
| Peaking | 1797 Hz | 1.85 | -2.5 dB |
| Peaking | 2903 Hz | 3.98 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Lady%20Gaga/Monster%20Lady%20Gaga.png)
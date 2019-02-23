# Monster Beats by Dr
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.2; 31 -3.4; 34 -5.4; 37 -6.3; 41 -6.8; 45 -7.2; 49 -7.3; 54 -7.0; 60 -7.1; 66 -7.5; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.7; 106 -8.9; 116 -9.1; 128 -9.1; 141 -9.3; 155 -9.4; 170 -9.1; 187 -9.2; 206 -8.6; 227 -8.3; 249 -8.3; 274 -8.1; 302 -7.9; 332 -7.5; 365 -6.9; 402 -6.7; 442 -6.1; 486 -5.4; 535 -4.4; 588 -3.3; 647 -1.9; 712 -1.4; 783 -1.4; 861 -2.2; 947 -3.7; 1042 -5.1; 1146 -6.3; 1261 -7.5; 1387 -9.3; 1526 -11.0; 1678 -12.2; 1846 -12.5; 2031 -11.9; 2234 -10.0; 2457 -7.6; 2703 -4.9; 2973 -3.0; 3270 -1.1; 3597 -1.3; 3957 -0.5; 4353 -3.2; 4788 -6.8; 5267 -7.9; 5793 -4.5; 6373 -1.3; 7010 -4.0; 7711 -6.9; 8482 -11.3; 9330 -10.7; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats by Dr GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats by Dr ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 2.95 | 6.8 dB  |
| Peaking | 765 Hz  | 2.15 | 6.3 dB  |
| Peaking | 1872 Hz | 1.62 | -8.0 dB |
| Peaking | 3406 Hz | 1.64 | 7.2 dB  |
| Peaking | 8841 Hz | 6.4  | -6.4 dB |
| Peaking | 29 Hz   | 3.43 | 1.9 dB  |
| Peaking | 90 Hz   | 0.63 | -1.1 dB |
| Peaking | 165 Hz  | 0.97 | -2.4 dB |
| Peaking | 5132 Hz | 5.71 | -3.9 dB |
| Peaking | 6421 Hz | 5.87 | 5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Beats%20by%20Dr/Monster%20Beats%20by%20Dr.png)
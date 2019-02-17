# Monster Beats by Dr
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -2.3; 31 -5.2; 34 -7.4; 37 -8.2; 41 -8.8; 45 -9.2; 49 -9.2; 54 -8.9; 60 -9.1; 66 -9.5; 72 -9.9; 79 -10.2; 87 -10.4; 96 -10.6; 106 -10.8; 116 -11.0; 128 -11.0; 141 -11.2; 155 -11.4; 170 -11.1; 187 -11.2; 206 -10.5; 227 -10.3; 249 -10.2; 274 -10.1; 302 -9.8; 332 -9.4; 365 -8.9; 402 -8.7; 442 -8.1; 486 -7.4; 535 -6.4; 588 -5.2; 647 -3.9; 712 -3.3; 783 -3.4; 861 -4.2; 947 -5.7; 1042 -7.0; 1146 -8.2; 1261 -9.5; 1387 -11.2; 1526 -13.0; 1678 -14.1; 1846 -14.4; 2031 -13.8; 2234 -12.0; 2457 -9.6; 2703 -6.9; 2973 -5.0; 3270 -3.1; 3597 -3.2; 3957 -1.1; 4353 -5.2; 4788 -8.7; 5267 -9.8; 5793 -6.4; 6373 -2.3; 7010 -4.0; 7711 -8.6; 8482 -13.2; 9330 -12.6; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats by Dr GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats by Dr ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 2.72 | 7.5 dB  |
| Peaking | 126 Hz  | 0.56 | -5.0 dB |
| Peaking | 1834 Hz | 2.34 | -9.1 dB |
| Peaking | 3604 Hz | 3.14 | 5.6 dB  |
| Peaking | 8861 Hz | 5.53 | -8.3 dB |
| Peaking | 746 Hz  | 2.66 | 4.6 dB  |
| Peaking | 1403 Hz | 4.4  | -1.9 dB |
| Peaking | 5158 Hz | 5.57 | -4.4 dB |
| Peaking | 6566 Hz | 6.56 | 5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Beats%20by%20Dr/Monster%20Beats%20by%20Dr.png)
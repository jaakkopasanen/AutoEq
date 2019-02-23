# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.4; 37 -2.2; 41 -3.3; 45 -4.2; 49 -5.1; 54 -6.1; 60 -7.1; 66 -8.1; 72 -8.9; 79 -9.7; 87 -10.3; 96 -10.9; 106 -11.3; 116 -11.3; 128 -11.4; 141 -11.3; 155 -11.3; 170 -11.1; 187 -10.7; 206 -10.2; 227 -9.8; 249 -9.3; 274 -8.9; 302 -8.5; 332 -8.0; 365 -7.5; 402 -6.9; 442 -6.7; 486 -6.3; 535 -6.0; 588 -5.7; 647 -5.4; 712 -5.4; 783 -5.2; 861 -5.3; 947 -5.4; 1042 -5.5; 1146 -5.7; 1261 -6.0; 1387 -6.8; 1526 -7.8; 1678 -8.7; 1846 -9.5; 2031 -10.1; 2234 -9.9; 2457 -8.4; 2703 -6.1; 2973 -3.6; 3270 -2.0; 3597 -1.3; 3957 -3.8; 4353 -5.1; 4788 -6.6; 5267 -4.4; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.88 | 6.9 dB  |
| Peaking | 121 Hz  | 0.75 | -5.8 dB |
| Peaking | 2099 Hz | 2.99 | -4.6 dB |
| Peaking | 3394 Hz | 3.37 | 5.8 dB  |
| Peaking | 6163 Hz | 5.02 | 6.2 dB  |
| Peaking | 632 Hz  | 2.23 | 1.2 dB  |
| Peaking | 982 Hz  | 1.59 | 1.3 dB  |
| Peaking | 1638 Hz | 4.4  | -1.2 dB |
| Peaking | 9128 Hz | 6.98 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)
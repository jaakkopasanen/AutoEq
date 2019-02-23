# Sleek SA6 Neutral
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.3; 25 -5.5; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.5; 79 -8.8; 87 -9.1; 96 -9.4; 106 -9.7; 116 -9.9; 128 -10.2; 141 -10.5; 155 -10.8; 170 -10.9; 187 -11.1; 206 -11.0; 227 -11.0; 249 -11.0; 274 -10.8; 302 -10.6; 332 -10.3; 365 -10.2; 402 -10.2; 442 -10.1; 486 -9.8; 535 -9.4; 588 -9.0; 647 -8.6; 712 -8.4; 783 -8.0; 861 -7.8; 947 -7.9; 1042 -8.3; 1146 -8.6; 1261 -8.9; 1387 -9.3; 1526 -9.7; 1678 -9.9; 1846 -10.1; 2031 -9.7; 2234 -8.9; 2457 -7.4; 2703 -4.9; 2973 -2.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sleek SA6 Neutral GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA6 Neutral ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.43 | 1.7 dB  |
| Peaking | 101 Hz  | 0.71 | -0.8 dB |
| Peaking | 234 Hz  | 0.45 | -4.2 dB |
| Peaking | 1971 Hz | 1.3  | -6.3 dB |
| Peaking | 3843 Hz | 0.94 | 8.3 dB  |
| Peaking | 2461 Hz | 6.99 | -0.8 dB |
| Peaking | 3109 Hz | 5.81 | 1.7 dB  |
| Peaking | 4004 Hz | 3.39 | -1.2 dB |
| Peaking | 6272 Hz | 2.55 | 4.9 dB  |
| Peaking | 7450 Hz | 1.54 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA6%20Neutral/Sleek%20SA6%20Neutral.png)
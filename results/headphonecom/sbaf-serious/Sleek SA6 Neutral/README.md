# Sleek SA6 Neutral
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.7; 25 -3.9; 28 -4.1; 31 -4.3; 34 -4.5; 37 -4.7; 41 -4.9; 45 -5.2; 49 -5.4; 54 -5.7; 60 -6.1; 66 -6.3; 72 -6.8; 79 -7.2; 87 -7.5; 96 -7.8; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.3; 187 -9.4; 206 -9.3; 227 -9.3; 249 -9.3; 274 -9.1; 302 -8.9; 332 -8.6; 365 -8.5; 402 -8.6; 442 -8.4; 486 -8.1; 535 -7.8; 588 -7.3; 647 -6.9; 712 -6.7; 783 -6.3; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.7; 1526 -8.1; 1678 -8.3; 1846 -8.4; 2031 -8.1; 2234 -7.3; 2457 -5.7; 2703 -3.2; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sleek SA6 Neutral GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA6 Neutral ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.42 | 0.3 dB  |
| Peaking | 20 Hz   | 0.45 | 2.8 dB  |
| Peaking | 200 Hz  | 0.57 | -3.1 dB |
| Peaking | 1956 Hz | 1.75 | -4.7 dB |
| Peaking | 3853 Hz | 0.9  | 7.5 dB  |
| Peaking | 841 Hz  | 3.62 | 0.9 dB  |
| Peaking | 2989 Hz | 6.21 | 2.1 dB  |
| Peaking | 5999 Hz | 0.68 | -2.5 dB |
| Peaking | 6249 Hz | 2    | 5.5 dB  |
| Peaking | 7544 Hz | 2.94 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA6%20Neutral/Sleek%20SA6%20Neutral.png)
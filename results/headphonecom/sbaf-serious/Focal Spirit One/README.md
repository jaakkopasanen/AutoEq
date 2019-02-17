# Focal Spirit One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.9; 28 -10.9; 31 -11.0; 34 -11.0; 37 -11.0; 41 -10.9; 45 -11.0; 49 -11.1; 54 -11.1; 60 -11.1; 66 -11.1; 72 -11.2; 79 -11.1; 87 -10.9; 96 -10.5; 106 -11.2; 116 -12.3; 128 -12.7; 141 -12.7; 155 -12.5; 170 -12.3; 187 -12.4; 206 -11.9; 227 -11.4; 249 -10.9; 274 -10.4; 302 -9.7; 332 -9.3; 365 -8.8; 402 -8.6; 442 -8.8; 486 -8.8; 535 -8.6; 588 -8.5; 647 -8.2; 712 -7.7; 783 -7.1; 861 -6.7; 947 -6.4; 1042 -6.0; 1146 -7.0; 1261 -6.9; 1387 -7.0; 1526 -7.4; 1678 -7.4; 1846 -6.8; 2031 -5.7; 2234 -4.4; 2457 -2.9; 2703 -1.7; 2973 -1.1; 3270 -1.2; 3597 -2.4; 3957 -4.5; 4353 -5.5; 4788 -5.4; 5267 -4.2; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.12 | -3.6 dB |
| Peaking | 43 Hz    | 1.1  | -2.4 dB |
| Peaking | 159 Hz   | 0.45 | -6.1 dB |
| Peaking | 3017 Hz  | 2.93 | 5.6 dB  |
| Peaking | 6180 Hz  | 5.06 | 6.2 dB  |
| Peaking | 348 Hz   | 2.82 | 0.9 dB  |
| Peaking | 573 Hz   | 3.1  | -0.9 dB |
| Peaking | 1622 Hz  | 4.06 | -1.8 dB |
| Peaking | 22050 Hz | 1.84 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Focal%20Spirit%20One/Focal%20Spirit%20One.png)
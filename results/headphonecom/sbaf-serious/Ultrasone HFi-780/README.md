# Ultrasone HFi-780
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -0.9; 72 -0.7; 79 -0.6; 87 -0.6; 96 -0.8; 106 -0.8; 116 -0.6; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -1.8; 274 -3.3; 302 -5.2; 332 -6.6; 365 -7.0; 402 -7.6; 442 -7.7; 486 -7.5; 535 -7.0; 588 -6.4; 647 -6.1; 712 -5.9; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -5.9; 1261 -6.9; 1387 -7.9; 1526 -8.4; 1678 -8.4; 1846 -8.1; 2031 -7.6; 2234 -0.8; 2457 -1.9; 2703 -3.4; 2973 -3.7; 3270 -4.2; 3597 -5.3; 3957 -4.0; 4353 -0.7; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -9.2; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFi-780 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 66 Hz   | 0.21 | 6.7 dB   |
| Peaking | 1136 Hz | 0.23 | -1.9 dB  |
| Peaking | 2361 Hz | 6.07 | 6.7 dB   |
| Peaking | 5665 Hz | 1.07 | 8.2 dB   |
| Peaking | 8759 Hz | 1.29 | -4.2 dB  |
| Peaking | 19 Hz   | 2.06 | 1.2 dB   |
| Peaking | 228 Hz  | 1.01 | 8.6 dB   |
| Peaking | 344 Hz  | 0.56 | -10.9 dB |
| Peaking | 651 Hz  | 0.52 | 6.0 dB   |
| Peaking | 1668 Hz | 2.29 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 5.3 dB  |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-780/Ultrasone%20HFi-780.png)
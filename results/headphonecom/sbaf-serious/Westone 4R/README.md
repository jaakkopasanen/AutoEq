# Westone 4R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.4; 25 -5.8; 28 -6.3; 31 -6.8; 34 -7.2; 37 -7.5; 41 -7.9; 45 -8.3; 49 -8.7; 54 -9.1; 60 -9.5; 66 -10.0; 72 -10.3; 79 -10.8; 87 -11.1; 96 -11.4; 106 -11.6; 116 -11.9; 128 -12.2; 141 -12.5; 155 -12.7; 170 -12.9; 187 -12.9; 206 -12.9; 227 -12.8; 249 -12.7; 274 -12.5; 302 -12.2; 332 -11.8; 365 -11.3; 402 -10.9; 442 -10.4; 486 -9.9; 535 -9.3; 588 -8.5; 647 -7.8; 712 -7.0; 783 -6.4; 861 -5.9; 947 -5.8; 1042 -6.0; 1146 -6.4; 1261 -6.8; 1387 -7.2; 1526 -7.3; 1678 -7.1; 1846 -6.4; 2031 -5.4; 2234 -4.2; 2457 -3.1; 2703 -2.2; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -12.4; 10263 -14.6; 11289 -9.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.35 | 2.3 dB   |
| Peaking | 126 Hz   | 0.48 | -4.9 dB  |
| Peaking | 294 Hz   | 0.86 | -3.3 dB  |
| Peaking | 4547 Hz  | 0.83 | 7.1 dB   |
| Peaking | 10004 Hz | 3.25 | -10.6 dB |
| Peaking | 890 Hz   | 2.83 | 1.6 dB   |
| Peaking | 1609 Hz  | 2.19 | -2.1 dB  |
| Peaking | 2963 Hz  | 2.62 | 1.9 dB   |
| Peaking | 5713 Hz  | 1.26 | -1.7 dB  |
| Peaking | 6059 Hz  | 3.99 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%204R/Westone%204R.png)
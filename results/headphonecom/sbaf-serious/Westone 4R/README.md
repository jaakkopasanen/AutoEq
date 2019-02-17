# Westone 4R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.9; 25 -6.3; 28 -6.8; 31 -7.3; 34 -7.7; 37 -8.0; 41 -8.4; 45 -8.8; 49 -9.1; 54 -9.6; 60 -10.0; 66 -10.5; 72 -10.8; 79 -11.3; 87 -11.6; 96 -11.9; 106 -12.1; 116 -12.4; 128 -12.7; 141 -13.0; 155 -13.2; 170 -13.4; 187 -13.4; 206 -13.4; 227 -13.3; 249 -13.2; 274 -13.0; 302 -12.7; 332 -12.3; 365 -11.8; 402 -11.4; 442 -10.9; 486 -10.4; 535 -9.8; 588 -9.0; 647 -8.3; 712 -7.5; 783 -6.9; 861 -6.4; 947 -6.3; 1042 -6.5; 1146 -6.9; 1261 -7.3; 1387 -7.7; 1526 -7.8; 1678 -7.6; 1846 -6.9; 2031 -5.8; 2234 -4.7; 2457 -3.5; 2703 -2.7; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -12.9; 10263 -15.1; 11289 -10.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 116 Hz   | 0.52 | -4.1 dB  |
| Peaking | 340 Hz   | 0.5  | -5.7 dB  |
| Peaking | 1687 Hz  | 0.97 | -8.6 dB  |
| Peaking | 2808 Hz  | 0.26 | 9.2 dB   |
| Peaking | 9904 Hz  | 2.35 | -13.3 dB |
| Peaking | 20 Hz    | 2.24 | 1.7 dB   |
| Peaking | 6299 Hz  | 4.86 | 1.3 dB   |
| Peaking | 7356 Hz  | 7.97 | -1.9 dB  |
| Peaking | 12012 Hz | 7.51 | 2.0 dB   |
| Peaking | 15616 Hz | 0.68 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%204R/Westone%204R.png)
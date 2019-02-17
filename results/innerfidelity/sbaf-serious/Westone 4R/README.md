# Westone 4R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.0; 25 -4.5; 28 -5.1; 31 -5.6; 34 -6.1; 37 -6.5; 41 -7.0; 45 -7.4; 49 -7.7; 54 -8.2; 60 -8.6; 66 -9.1; 72 -9.6; 79 -10.0; 87 -10.6; 96 -11.1; 106 -11.4; 116 -11.7; 128 -12.1; 141 -12.3; 155 -12.5; 170 -12.6; 187 -12.7; 206 -12.7; 227 -12.6; 249 -12.6; 274 -12.4; 302 -12.2; 332 -11.9; 365 -11.5; 402 -11.1; 442 -10.6; 486 -10.3; 535 -9.7; 588 -8.8; 647 -8.1; 712 -7.6; 783 -6.8; 861 -6.5; 947 -6.4; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.5; 1526 -7.6; 1678 -7.3; 1846 -6.5; 2031 -5.4; 2234 -4.5; 2457 -3.3; 2703 -2.4; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.3; 9330 -12.7; 10263 -13.9; 11289 -8.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.07 | 3.5 dB   |
| Peaking | 110 Hz  | 0.68 | -3.2 dB  |
| Peaking | 265 Hz  | 0.6  | -5.0 dB  |
| Peaking | 4611 Hz | 0.84 | 7.2 dB   |
| Peaking | 9806 Hz | 2.99 | -10.0 dB |
| Peaking | 867 Hz  | 2.81 | 1.3 dB   |
| Peaking | 1597 Hz | 2.15 | -2.0 dB  |
| Peaking | 3087 Hz | 2.07 | 2.5 dB   |
| Peaking | 4309 Hz | 1    | -1.5 dB  |
| Peaking | 6142 Hz | 5.14 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%204R/Westone%204R.png)
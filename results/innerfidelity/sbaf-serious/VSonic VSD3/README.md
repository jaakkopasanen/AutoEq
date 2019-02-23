# VSonic VSD3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.9; 25 -6.2; 28 -6.6; 31 -7.0; 34 -7.2; 37 -7.5; 41 -7.7; 45 -7.9; 49 -8.2; 54 -8.4; 60 -8.7; 66 -9.0; 72 -9.4; 79 -9.7; 87 -10.0; 96 -10.4; 106 -10.6; 116 -10.6; 128 -10.8; 141 -10.9; 155 -11.0; 170 -10.9; 187 -10.7; 206 -10.6; 227 -10.3; 249 -10.1; 274 -9.8; 302 -9.5; 332 -9.2; 365 -8.8; 402 -8.5; 442 -8.0; 486 -7.8; 535 -7.3; 588 -6.7; 647 -6.4; 712 -6.1; 783 -5.7; 861 -5.6; 947 -5.5; 1042 -5.4; 1146 -5.5; 1261 -5.5; 1387 -5.5; 1526 -5.4; 1678 -5.2; 1846 -4.8; 2031 -4.3; 2234 -3.9; 2457 -2.9; 2703 -2.8; 2973 -1.7; 3270 -0.7; 3597 -0.5; 3957 -0.8; 4353 -3.1; 4788 -4.7; 5267 -5.9; 5793 -7.1; 6373 -6.0; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -10.8; 11289 -9.9; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 0.68 | -4.0 dB |
| Peaking | 255 Hz   | 1.24 | -2.0 dB |
| Peaking | 3289 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8762 Hz  | 3.65 | 1.0 dB  |
| Peaking | 10452 Hz | 3.23 | -5.1 dB |
| Peaking | 19 Hz    | 2    | 1.3 dB  |
| Peaking | 930 Hz   | 1.83 | 1.1 dB  |
| Peaking | 3887 Hz  | 7.66 | 1.6 dB  |
| Peaking | 5959 Hz  | 2.65 | -2.5 dB |
| Peaking | 6870 Hz  | 5.98 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3/VSonic%20VSD3.png)
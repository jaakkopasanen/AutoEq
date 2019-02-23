# Beyerdynamic T50p sn16912
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.4; 31 -2.1; 34 -2.7; 37 -3.2; 41 -3.8; 45 -4.2; 49 -4.7; 54 -5.3; 60 -5.9; 66 -6.3; 72 -6.5; 79 -6.7; 87 -6.6; 96 -7.0; 106 -6.4; 116 -5.9; 128 -6.2; 141 -5.8; 155 -5.6; 170 -6.0; 187 -7.7; 206 -9.7; 227 -11.2; 249 -12.1; 274 -12.2; 302 -13.2; 332 -14.1; 365 -13.7; 402 -13.2; 442 -12.9; 486 -12.5; 535 -12.0; 588 -11.4; 647 -11.1; 712 -10.1; 783 -9.4; 861 -9.5; 947 -9.2; 1042 -9.1; 1146 -8.8; 1261 -8.6; 1387 -8.8; 1526 -9.0; 1678 -8.9; 1846 -8.2; 2031 -7.0; 2234 -5.1; 2457 -2.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.7; 9330 -10.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sn16912 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sn16912 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.75 | 6.2 dB  |
| Peaking | 373 Hz  | 1.03 | -7.6 dB |
| Peaking | 1742 Hz | 0.72 | -9.6 dB |
| Peaking | 3016 Hz | 0.5  | 11.6 dB |
| Peaking | 8801 Hz | 3.38 | -8.2 dB |
| Peaking | 161 Hz  | 2.98 | 2.8 dB  |
| Peaking | 231 Hz  | 3.4  | -1.9 dB |
| Peaking | 2657 Hz | 5.89 | 2.2 dB  |
| Peaking | 5305 Hz | 0.42 | -1.0 dB |
| Peaking | 6065 Hz | 2.66 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | 2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -5.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sn16912/Beyerdynamic%20T50p%20sn16912.png)
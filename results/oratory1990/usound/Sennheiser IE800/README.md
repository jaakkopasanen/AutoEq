# Sennheiser IE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.5; 28 -11.5; 31 -11.5; 34 -11.4; 37 -11.4; 41 -11.4; 45 -11.4; 49 -11.4; 54 -11.4; 60 -11.4; 66 -11.4; 72 -11.5; 79 -11.5; 87 -11.5; 96 -11.5; 106 -11.4; 116 -11.3; 128 -11.3; 141 -11.4; 155 -11.4; 170 -11.3; 187 -11.1; 206 -10.7; 227 -10.3; 249 -9.9; 274 -9.5; 302 -9.1; 332 -8.8; 365 -8.5; 402 -8.1; 442 -7.9; 486 -7.6; 535 -7.4; 588 -7.2; 647 -7.0; 712 -6.8; 783 -6.7; 861 -6.6; 947 -6.8; 1042 -7.0; 1146 -7.1; 1261 -7.2; 1387 -7.1; 1526 -6.5; 1678 -5.6; 1846 -4.3; 2031 -3.0; 2234 -1.7; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.8; 5267 -3.7; 5793 -4.1; 6373 -3.2; 7010 -5.7; 7711 -7.5; 8482 -8.8; 9330 -10.9; 10263 -13.1; 11289 -13.4; 12418 -13.7; 13660 -15.5; 15026 -15.7; 16529 -12.9; 18182 -11.6; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.26 | -4.7 dB  |
| Peaking | 157 Hz   | 0.43 | -4.1 dB  |
| Peaking | 1383 Hz  | 1.08 | -5.7 dB  |
| Peaking | 4238 Hz  | 0.33 | 11.8 dB  |
| Peaking | 12123 Hz | 0.33 | -12.9 dB |
| Peaking | 1875 Hz  | 2.44 | -0.5 dB  |
| Peaking | 2459 Hz  | 3.48 | 1.1 dB   |
| Peaking | 2479 Hz  | 0.61 | 0.5 dB   |
| Peaking | 2894 Hz  | 1.62 | -0.2 dB  |
| Peaking | 2974 Hz  | 1.91 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 16000 Hz | 1.41 | -12.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20IE800/Sennheiser%20IE800.png)
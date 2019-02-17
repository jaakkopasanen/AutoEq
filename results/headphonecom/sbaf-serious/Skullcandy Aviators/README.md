# Skullcandy Aviators
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.6; 25 -2.6; 28 -4.1; 31 -5.3; 34 -6.5; 37 -7.5; 41 -8.7; 45 -9.8; 49 -10.6; 54 -11.4; 60 -12.3; 66 -13.3; 72 -14.0; 79 -14.5; 87 -14.8; 96 -15.2; 106 -15.5; 116 -15.7; 128 -15.7; 141 -15.9; 155 -15.8; 170 -15.8; 187 -15.8; 206 -15.7; 227 -15.6; 249 -15.3; 274 -14.6; 302 -14.0; 332 -14.1; 365 -13.7; 402 -13.5; 442 -13.2; 486 -12.9; 535 -12.5; 588 -11.4; 647 -10.4; 712 -10.6; 783 -8.5; 861 -6.1; 947 -4.5; 1042 -5.0; 1146 -6.1; 1261 -8.3; 1387 -10.4; 1526 -11.5; 1678 -12.2; 1846 -12.2; 2031 -11.6; 2234 -11.0; 2457 -10.4; 2703 -10.4; 2973 -11.4; 3270 -12.0; 3597 -11.4; 3957 -13.2; 4353 -17.1; 4788 -16.9; 5267 -12.9; 5793 -9.0; 6373 -6.1; 7010 -5.9; 7711 -6.8; 8482 -11.5; 9330 -14.8; 10263 -13.6; 11289 -11.9; 12418 -11.3; 13660 -10.8; 15026 -8.6; 16529 -4.9; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Aviators GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Aviators ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 133 Hz   | 0.47 | -11.3 dB |
| Peaking | 422 Hz   | 1.17 | -4.7 dB  |
| Peaking | 1991 Hz  | 1.43 | -6.7 dB  |
| Peaking | 4473 Hz  | 3.11 | -11.8 dB |
| Peaking | 10825 Hz | 1.35 | -8.8 dB  |
| Peaking | 21 Hz    | 2.39 | 6.1 dB   |
| Peaking | 991 Hz   | 2.65 | 7.5 dB   |
| Peaking | 1001 Hz  | 1.06 | -3.6 dB  |
| Peaking | 7173 Hz  | 3.55 | 3.8 dB   |
| Peaking | 9118 Hz  | 5.95 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -7.4 dB |
| Peaking | 125 Hz   | 1.41 | -9.1 dB |
| Peaking | 250 Hz   | 1.41 | -8.0 dB |
| Peaking | 500 Hz   | 1.41 | -6.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | -7.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Aviators/Skullcandy%20Aviators.png)
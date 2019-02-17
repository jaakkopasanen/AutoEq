# Cougar Immersa
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.3; 25 -2.0; 28 -2.9; 31 -3.8; 34 -4.5; 37 -5.1; 41 -5.9; 45 -6.6; 49 -7.2; 54 -7.9; 60 -8.7; 66 -9.6; 72 -10.5; 79 -11.5; 87 -12.5; 96 -13.3; 106 -13.9; 116 -14.3; 128 -14.6; 141 -14.7; 155 -14.7; 170 -14.4; 187 -14.1; 206 -13.6; 227 -13.1; 249 -12.6; 274 -12.2; 302 -11.9; 332 -11.4; 365 -10.6; 402 -9.6; 442 -8.5; 486 -7.7; 535 -6.9; 588 -6.1; 647 -5.3; 712 -4.9; 783 -4.7; 861 -4.4; 947 -3.9; 1042 -3.0; 1146 -1.6; 1261 -0.5; 1387 -0.5; 1526 -0.6; 1678 -1.0; 1846 -2.7; 2031 -4.6; 2234 -4.5; 2457 -3.5; 2703 -3.0; 2973 -3.1; 3270 -4.1; 3597 -6.1; 3957 -7.4; 4353 -7.7; 4788 -5.3; 5267 -5.3; 5793 -4.5; 6373 -5.6; 7010 -4.9; 7711 -6.5; 8482 -9.0; 9330 -8.9; 10263 -6.1; 11289 -4.6; 12418 -4.5; 13660 -4.7; 15026 -6.3; 16529 -7.5; 18182 -7.8; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cougar Immersa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cougar Immersa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.59 | 3.8 dB   |
| Peaking | 126 Hz   | 0.63 | -10.9 dB |
| Peaking | 304 Hz   | 1.29 | -4.3 dB  |
| Peaking | 8747 Hz  | 2.37 | -5.2 dB  |
| Peaking | 20173 Hz | 0.39 | -7.3 dB  |
| Peaking | 1421 Hz  | 2.17 | 4.0 dB   |
| Peaking | 2080 Hz  | 5.82 | -2.2 dB  |
| Peaking | 2881 Hz  | 4.73 | 1.3 dB   |
| Peaking | 4099 Hz  | 3.55 | -4.4 dB  |
| Peaking | 11948 Hz | 2.26 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB   |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -10.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB  |
| Peaking | 500 Hz   | 1.41 | -3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -4.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cougar%20Immersa/Cougar%20Immersa.png)
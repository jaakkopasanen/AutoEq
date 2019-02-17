# Woodees iESW101B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.2; 25 -11.2; 28 -11.1; 31 -11.0; 34 -10.9; 37 -10.8; 41 -10.7; 45 -10.6; 49 -10.6; 54 -10.5; 60 -10.4; 66 -10.4; 72 -10.3; 79 -10.2; 87 -10.1; 96 -9.9; 106 -9.7; 116 -9.4; 128 -9.2; 141 -8.9; 155 -8.5; 170 -8.1; 187 -7.7; 206 -7.1; 227 -6.6; 249 -6.0; 274 -5.4; 302 -4.7; 332 -4.1; 365 -3.3; 402 -2.7; 442 -2.0; 486 -1.5; 535 -1.0; 588 -0.7; 647 -0.5; 712 -0.6; 783 -0.9; 861 -1.1; 947 -1.5; 1042 -2.1; 1146 -2.5; 1261 -3.1; 1387 -3.8; 1526 -4.8; 1678 -5.5; 1846 -6.0; 2031 -6.6; 2234 -7.4; 2457 -8.5; 2703 -9.4; 2973 -7.5; 3270 -3.5; 3597 -0.6; 3957 -0.8; 4353 -3.1; 4788 -5.2; 5267 -8.1; 5793 -13.7; 6373 -7.5; 7010 -3.2; 7711 -1.7; 8482 -2.6; 9330 -6.2; 10263 -6.2; 11289 -1.9; 12418 -1.9; 13660 -1.9; 15026 -1.9; 16529 -3.1; 18182 -1.9; 20000 -1.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW101B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW101B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.28 | -9.1 dB  |
| Peaking | 145 Hz   | 0.92 | -3.8 dB  |
| Peaking | 2412 Hz  | 2.23 | -7.1 dB  |
| Peaking | 5785 Hz  | 5.62 | -12.0 dB |
| Peaking | 16562 Hz | 2.48 | -1.0 dB  |
| Peaking | 670 Hz   | 0.83 | 5.8 dB   |
| Peaking | 740 Hz   | 0.43 | -3.7 dB  |
| Peaking | 3752 Hz  | 5.11 | 4.4 dB   |
| Peaking | 4885 Hz  | 5.82 | -0.8 dB  |
| Peaking | 9807 Hz  | 7.15 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW101B/Woodees%20iESW101B.png)
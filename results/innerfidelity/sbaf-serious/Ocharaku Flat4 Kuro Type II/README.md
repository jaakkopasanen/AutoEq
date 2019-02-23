# Ocharaku Flat4 Kuro Type II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.6; 25 -5.8; 28 -6.1; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.8; 45 -7.0; 49 -7.2; 54 -7.3; 60 -7.5; 66 -7.8; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.7; 106 -8.9; 116 -8.8; 128 -8.9; 141 -8.9; 155 -8.9; 170 -8.8; 187 -8.6; 206 -8.4; 227 -8.0; 249 -7.8; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.4; 402 -6.1; 442 -5.7; 486 -5.6; 535 -5.4; 588 -5.0; 647 -5.0; 712 -5.2; 783 -5.2; 861 -5.7; 947 -6.3; 1042 -6.9; 1146 -7.3; 1261 -7.2; 1387 -7.0; 1526 -5.8; 1678 -4.1; 1846 -1.5; 2031 -0.5; 2234 -0.5; 2457 -1.0; 2703 -2.8; 2973 -5.3; 3270 -7.1; 3597 -6.2; 3957 -5.8; 4353 -8.0; 4788 -11.5; 5267 -11.4; 5793 -0.6; 6373 -1.0; 7010 -9.0; 7711 -14.6; 8482 -14.3; 9330 -13.1; 10263 -9.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -6.6; 18182 -6.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat4 Kuro Type II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat4 Kuro Type II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 125 Hz   | 0.93 | -2.7 dB  |
| Peaking | 2176 Hz  | 2.66 | 7.0 dB   |
| Peaking | 5064 Hz  | 5.58 | -11.0 dB |
| Peaking | 6045 Hz  | 3.18 | 12.4 dB  |
| Peaking | 8010 Hz  | 2.33 | -11.4 dB |
| Peaking | 19 Hz    | 2.12 | 1.3 dB   |
| Peaking | 636 Hz   | 1.58 | 1.7 dB   |
| Peaking | 1223 Hz  | 3.01 | -1.9 dB  |
| Peaking | 11141 Hz | 9.92 | 1.8 dB   |
| Peaking | 12471 Hz | 4.55 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ocharaku%20Flat4%20Kuro%20Type%20II/Ocharaku%20Flat4%20Kuro%20Type%20II.png)
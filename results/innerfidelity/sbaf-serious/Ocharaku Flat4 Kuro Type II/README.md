# Ocharaku Flat4 Kuro Type II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.6; 28 -5.9; 31 -6.1; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.1; 60 -7.3; 66 -7.6; 72 -7.8; 79 -8.1; 87 -8.3; 96 -8.6; 106 -8.7; 116 -8.7; 128 -8.7; 141 -8.7; 155 -8.7; 170 -8.6; 187 -8.4; 206 -8.2; 227 -7.8; 249 -7.6; 274 -7.2; 302 -6.9; 332 -6.6; 365 -6.2; 402 -5.9; 442 -5.5; 486 -5.4; 535 -5.2; 588 -4.8; 647 -4.8; 712 -5.0; 783 -5.0; 861 -5.5; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -7.0; 1387 -6.8; 1526 -5.6; 1678 -3.9; 1846 -1.3; 2031 -0.5; 2234 -0.5; 2457 -0.8; 2703 -2.6; 2973 -5.1; 3270 -6.9; 3597 -6.0; 3957 -5.6; 4353 -7.8; 4788 -11.3; 5267 -11.2; 5793 -0.6; 6373 -1.0; 7010 -8.8; 7711 -14.4; 8482 -14.1; 9330 -12.9; 10263 -9.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat4 Kuro Type II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat4 Kuro Type II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 125 Hz   |  1.03 | -2.5 dB  |
| Peaking | 2178 Hz  |  2.5  | 6.9 dB   |
| Peaking | 5058 Hz  |  5.64 | -11.0 dB |
| Peaking | 6042 Hz  |  3.08 | 12.3 dB  |
| Peaking | 8000 Hz  |  2.35 | -11.3 dB |
| Peaking | 20 Hz    |  1.87 | 1.5 dB   |
| Peaking | 635 Hz   |  1.52 | 1.9 dB   |
| Peaking | 1228 Hz  |  3.01 | -1.8 dB  |
| Peaking | 11028 Hz | 10.77 | 1.7 dB   |
| Peaking | 12492 Hz |  4.5  | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ocharaku%20Flat4%20Kuro%20Type%20II/Ocharaku%20Flat4%20Kuro%20Type%20II.png)
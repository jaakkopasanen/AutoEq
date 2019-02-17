# Music Hall DeBe
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.0; 41 -1.5; 45 -1.9; 49 -2.2; 54 -2.7; 60 -3.1; 66 -3.6; 72 -4.0; 79 -4.5; 87 -5.2; 96 -5.7; 106 -6.2; 116 -6.6; 128 -7.2; 141 -7.6; 155 -8.1; 170 -8.3; 187 -8.3; 206 -8.8; 227 -9.1; 249 -9.4; 274 -9.3; 302 -9.1; 332 -9.3; 365 -9.1; 402 -8.8; 442 -8.7; 486 -8.3; 535 -7.2; 588 -5.5; 647 -4.3; 712 -4.4; 783 -4.9; 861 -5.7; 947 -6.2; 1042 -6.5; 1146 -6.4; 1261 -6.4; 1387 -6.2; 1526 -5.5; 1678 -4.3; 1846 -2.7; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.0; 5267 -3.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Music Hall DeBe GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Music Hall DeBe ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.36 | 6.3 dB  |
| Peaking | 424 Hz  | 0.27 | -3.9 dB |
| Peaking | 691 Hz  | 1.74 | 5.5 dB  |
| Peaking | 2194 Hz | 1.81 | 4.6 dB  |
| Peaking | 3852 Hz | 0.88 | 5.6 dB  |
| Peaking | 5025 Hz | 7.37 | -4.8 dB |
| Peaking | 6211 Hz | 2.14 | 6.0 dB  |
| Peaking | 7411 Hz | 1.59 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Music%20Hall%20DeBe/Music%20Hall%20DeBe.png)
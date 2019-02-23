# Lear LUF 4C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.7; 25 -4.8; 28 -5.0; 31 -5.2; 34 -5.3; 37 -5.5; 41 -5.7; 45 -5.9; 49 -6.1; 54 -6.4; 60 -6.7; 66 -6.9; 72 -7.1; 79 -7.5; 87 -7.8; 96 -8.0; 106 -8.1; 116 -8.0; 128 -8.0; 141 -7.8; 155 -7.5; 170 -7.0; 187 -6.4; 206 -5.8; 227 -5.1; 249 -4.6; 274 -4.1; 302 -3.7; 332 -3.4; 365 -3.2; 402 -3.2; 442 -3.0; 486 -3.1; 535 -3.1; 588 -2.8; 647 -3.0; 712 -3.3; 783 -3.3; 861 -3.8; 947 -4.4; 1042 -5.1; 1146 -5.9; 1261 -6.9; 1387 -8.4; 1526 -10.0; 1678 -11.1; 1846 -11.9; 2031 -12.9; 2234 -13.5; 2457 -12.5; 2703 -10.4; 2973 -7.1; 3270 -5.1; 3597 -4.1; 3957 -3.3; 4353 -0.5; 4788 -0.9; 5267 -6.7; 5793 -9.7; 6373 -6.8; 7010 -4.7; 7711 -6.0; 8482 -9.6; 9330 -11.3; 10263 -8.3; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear LUF 4C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF 4C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 614 Hz  | 0.78 | 4.2 dB   |
| Peaking | 2182 Hz | 1.28 | -10.0 dB |
| Peaking | 4864 Hz | 1.06 | 10.3 dB  |
| Peaking | 5661 Hz | 3.78 | -11.4 dB |
| Peaking | 9124 Hz | 3.41 | -7.3 dB  |
| Peaking | 15 Hz   | 0.38 | 1.9 dB   |
| Peaking | 115 Hz  | 0.76 | -2.4 dB  |
| Peaking | 283 Hz  | 1.7  | 1.6 dB   |
| Peaking | 3135 Hz | 5.61 | 2.4 dB   |
| Peaking | 3253 Hz | 2.65 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF%204C/Lear%20LUF%204C.png)
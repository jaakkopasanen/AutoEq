# Monster Solo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.9; 25 -11.2; 28 -11.5; 31 -11.8; 34 -12.1; 37 -12.4; 41 -12.7; 45 -13.0; 49 -13.1; 54 -13.4; 60 -14.0; 66 -14.5; 72 -14.9; 79 -15.1; 87 -15.2; 96 -14.9; 106 -14.4; 116 -14.9; 128 -16.2; 141 -17.1; 155 -16.9; 170 -16.0; 187 -16.0; 206 -15.1; 227 -13.8; 249 -12.3; 274 -11.0; 302 -10.2; 332 -9.5; 365 -8.5; 402 -7.5; 442 -6.5; 486 -5.9; 535 -5.7; 588 -5.6; 647 -5.9; 712 -6.2; 783 -6.6; 861 -6.8; 947 -6.7; 1042 -6.2; 1146 -5.5; 1261 -4.9; 1387 -4.6; 1526 -4.5; 1678 -4.4; 1846 -4.2; 2031 -4.0; 2234 -3.9; 2457 -3.7; 2703 -3.4; 2973 -3.0; 3270 -3.0; 3597 -3.6; 3957 -4.9; 4353 -6.3; 4788 -5.1; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Solo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.2  | -6.8 dB |
| Peaking | 67 Hz   | 0.55 | -7.0 dB |
| Peaking | 171 Hz  | 1.24 | -7.5 dB |
| Peaking | 3448 Hz | 0.44 | 3.2 dB  |
| Peaking | 520 Hz  | 2.84 | 1.7 dB  |
| Peaking | 912 Hz  | 3.69 | -1.2 dB |
| Peaking | 4418 Hz | 3.8  | -5.9 dB |
| Peaking | 5765 Hz | 1.64 | 7.6 dB  |
| Peaking | 7716 Hz | 1.28 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Solo/Monster%20Solo.png)
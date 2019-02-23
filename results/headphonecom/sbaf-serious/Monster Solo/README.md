# Monster Solo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.3; 25 -11.5; 28 -11.9; 31 -12.2; 34 -12.5; 37 -12.7; 41 -13.0; 45 -13.3; 49 -13.5; 54 -13.7; 60 -14.3; 66 -14.8; 72 -15.2; 79 -15.5; 87 -15.5; 96 -15.2; 106 -14.8; 116 -15.2; 128 -16.5; 141 -17.4; 155 -17.2; 170 -16.4; 187 -16.3; 206 -15.4; 227 -14.1; 249 -12.7; 274 -11.3; 302 -10.6; 332 -9.8; 365 -8.8; 402 -7.8; 442 -6.8; 486 -6.2; 535 -6.0; 588 -6.0; 647 -6.2; 712 -6.6; 783 -6.9; 861 -7.1; 947 -7.0; 1042 -6.6; 1146 -5.9; 1261 -5.2; 1387 -4.9; 1526 -4.8; 1678 -4.7; 1846 -4.6; 2031 -4.4; 2234 -4.2; 2457 -4.0; 2703 -3.7; 2973 -3.3; 3270 -3.3; 3597 -3.9; 3957 -5.2; 4353 -6.6; 4788 -5.4; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Solo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.98 | -7.1 dB |
| Peaking | 68 Hz   | 0.58 | -7.3 dB |
| Peaking | 171 Hz  | 1.26 | -7.9 dB |
| Peaking | 5800 Hz | 2.65 | 6.4 dB  |
| Peaking | 34 Hz   | 2.71 | -0.6 dB |
| Peaking | 514 Hz  | 3.83 | 1.6 dB  |
| Peaking | 3110 Hz | 0.73 | 3.0 dB  |
| Peaking | 4473 Hz | 4.31 | -4.6 dB |
| Peaking | 8083 Hz | 2.18 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -9.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Solo/Monster%20Solo.png)
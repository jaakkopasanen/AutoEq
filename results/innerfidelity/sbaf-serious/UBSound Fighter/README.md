# UBSound Fighter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.4; 25 -12.7; 28 -13.1; 31 -13.4; 34 -13.7; 37 -14.0; 41 -14.3; 45 -14.5; 49 -14.7; 54 -15.0; 60 -15.2; 66 -15.4; 72 -15.6; 79 -15.8; 87 -15.9; 96 -16.1; 106 -16.0; 116 -15.9; 128 -15.8; 141 -15.7; 155 -15.5; 170 -15.1; 187 -14.7; 206 -14.3; 227 -13.7; 249 -13.2; 274 -12.6; 302 -11.9; 332 -11.3; 365 -10.7; 402 -9.9; 442 -9.1; 486 -8.6; 535 -8.0; 588 -6.9; 647 -6.3; 712 -5.5; 783 -4.7; 861 -6.3; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -6.8; 1387 -7.7; 1526 -8.4; 1678 -8.9; 1846 -8.9; 2031 -7.9; 2234 -5.9; 2457 -2.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.5; 6373 -9.7; 7010 -5.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`UBSound Fighter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UBSound Fighter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.37 | -7.2 dB |
| Peaking | 136 Hz  | 0.8  | -5.1 dB |
| Peaking | 268 Hz  | 1.39 | -2.9 dB |
| Peaking | 1840 Hz | 2.41 | -5.4 dB |
| Peaking | 3317 Hz | 1.06 | 7.5 dB  |
| Peaking | 686 Hz  | 0.79 | -0.9 dB |
| Peaking | 736 Hz  | 2.76 | 3.0 dB  |
| Peaking | 3482 Hz | 6.17 | -1.2 dB |
| Peaking | 5410 Hz | 3.33 | 4.4 dB  |
| Peaking | 6317 Hz | 5.32 | -7.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UBSound%20Fighter/UBSound%20Fighter.png)
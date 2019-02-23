# UBSound Fighter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -12.0; 25 -12.3; 28 -12.7; 31 -13.0; 34 -13.3; 37 -13.6; 41 -13.9; 45 -14.1; 49 -14.3; 54 -14.6; 60 -14.8; 66 -15.0; 72 -15.2; 79 -15.4; 87 -15.5; 96 -15.7; 106 -15.6; 116 -15.5; 128 -15.4; 141 -15.3; 155 -15.1; 170 -14.7; 187 -14.3; 206 -13.9; 227 -13.3; 249 -12.8; 274 -12.2; 302 -11.5; 332 -10.9; 365 -10.3; 402 -9.5; 442 -8.7; 486 -8.2; 535 -7.6; 588 -6.5; 647 -5.9; 712 -5.1; 783 -4.3; 861 -5.9; 947 -5.9; 1042 -6.2; 1146 -6.4; 1261 -6.4; 1387 -7.3; 1526 -8.0; 1678 -8.5; 1846 -8.5; 2031 -7.5; 2234 -5.5; 2457 -2.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.1; 6373 -9.3; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`UBSound Fighter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UBSound Fighter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.37 | -6.9 dB |
| Peaking | 136 Hz  | 0.8  | -4.9 dB |
| Peaking | 267 Hz  | 1.4  | -2.7 dB |
| Peaking | 1893 Hz | 1.72 | -9.1 dB |
| Peaking | 2719 Hz | 0.78 | 9.4 dB  |
| Peaking | 739 Hz  | 3.67 | 2.5 dB  |
| Peaking | 4203 Hz | 0.11 | -0.5 dB |
| Peaking | 4622 Hz | 3.51 | 1.6 dB  |
| Peaking | 5527 Hz | 4.55 | 3.8 dB  |
| Peaking | 6352 Hz | 6.02 | -6.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UBSound%20Fighter/UBSound%20Fighter.png)
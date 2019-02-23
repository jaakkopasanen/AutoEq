# Teac CT-H02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.7; 25 -6.8; 28 -6.9; 31 -7.0; 34 -7.1; 37 -7.1; 41 -7.1; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.3; 66 -7.4; 72 -7.6; 79 -7.8; 87 -7.8; 96 -7.6; 106 -8.2; 116 -8.3; 128 -7.8; 141 -6.9; 155 -8.6; 170 -7.8; 187 -8.9; 206 -9.5; 227 -9.7; 249 -9.7; 274 -9.4; 302 -9.3; 332 -9.1; 365 -8.9; 402 -8.6; 442 -8.5; 486 -8.5; 535 -8.6; 588 -8.7; 647 -8.6; 712 -8.5; 783 -8.3; 861 -8.1; 947 -7.4; 1042 -7.1; 1146 -7.7; 1261 -7.8; 1387 -7.9; 1526 -8.2; 1678 -8.0; 1846 -7.1; 2031 -5.5; 2234 -4.7; 2457 -3.1; 2703 -1.9; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.4; 8482 -13.8; 9330 -14.8; 10263 -10.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teac CT-H02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 303 Hz   | 0.39 | -2.7 dB  |
| Peaking | 1656 Hz  | 1.98 | -2.7 dB  |
| Peaking | 3160 Hz  | 1.22 | 5.5 dB   |
| Peaking | 6018 Hz  | 1.44 | 6.2 dB   |
| Peaking | 8853 Hz  | 3.03 | -11.9 dB |
| Peaking | 145 Hz   | 2.59 | 1.7 dB   |
| Peaking | 193 Hz   | 0.45 | -0.9 dB  |
| Peaking | 407 Hz   | 2.07 | 1.0 dB   |
| Peaking | 9922 Hz  | 7.57 | -2.5 dB  |
| Peaking | 10950 Hz | 3.53 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)
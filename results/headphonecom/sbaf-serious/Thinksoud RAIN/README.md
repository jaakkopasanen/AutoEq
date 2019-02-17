# Thinksoud RAIN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.2; 23 -15.3; 25 -15.4; 28 -15.6; 31 -15.7; 34 -15.8; 37 -15.8; 41 -15.9; 45 -16.0; 49 -16.2; 54 -16.4; 60 -16.5; 66 -16.8; 72 -16.9; 79 -17.1; 87 -17.2; 96 -17.3; 106 -17.3; 116 -17.3; 128 -17.2; 141 -17.2; 155 -17.0; 170 -16.8; 187 -16.5; 206 -16.0; 227 -15.6; 249 -15.1; 274 -14.5; 302 -13.9; 332 -13.2; 365 -12.3; 402 -11.6; 442 -10.9; 486 -10.2; 535 -9.4; 588 -8.6; 647 -7.8; 712 -7.2; 783 -6.5; 861 -6.1; 947 -5.4; 1042 -4.9; 1146 -4.7; 1261 -4.7; 1387 -4.7; 1526 -4.8; 1678 -4.7; 1846 -4.3; 2031 -4.0; 2234 -3.9; 2457 -4.6; 2703 -5.9; 2973 -4.4; 3270 -1.6; 3597 -0.5; 3957 -2.2; 4353 -5.7; 4788 -9.5; 5267 -12.7; 5793 -6.4; 6373 -1.3; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksoud RAIN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksoud RAIN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.22 | -9.8 dB  |
| Peaking | 151 Hz  | 0.58 | -6.7 dB  |
| Peaking | 329 Hz  | 1    | -3.5 dB  |
| Peaking | 4798 Hz | 1.07 | 6.3 dB   |
| Peaking | 5105 Hz | 4.19 | -14.5 dB |
| Peaking | 1141 Hz | 2.3  | 1.1 dB   |
| Peaking | 2775 Hz | 7.09 | -2.8 dB  |
| Peaking | 3535 Hz | 5.35 | 2.9 dB   |
| Peaking | 6492 Hz | 5.08 | 5.8 dB   |
| Peaking | 6816 Hz | 1.18 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.5 dB |
| Peaking | 62 Hz    | 1.41 | -8.3 dB  |
| Peaking | 125 Hz   | 1.41 | -9.9 dB  |
| Peaking | 250 Hz   | 1.41 | -8.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksoud%20RAIN/Thinksoud%20RAIN.png)
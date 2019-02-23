# Thinksoud RAIN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.7; 25 -13.8; 28 -14.0; 31 -14.1; 34 -14.1; 37 -14.2; 41 -14.3; 45 -14.4; 49 -14.6; 54 -14.8; 60 -14.9; 66 -15.2; 72 -15.3; 79 -15.5; 87 -15.6; 96 -15.7; 106 -15.6; 116 -15.7; 128 -15.6; 141 -15.6; 155 -15.4; 170 -15.2; 187 -14.8; 206 -14.4; 227 -14.0; 249 -13.5; 274 -12.9; 302 -12.3; 332 -11.5; 365 -10.7; 402 -10.0; 442 -9.3; 486 -8.6; 535 -7.8; 588 -7.0; 647 -6.2; 712 -5.5; 783 -4.9; 861 -4.5; 947 -3.8; 1042 -3.2; 1146 -3.1; 1261 -3.1; 1387 -3.1; 1526 -3.2; 1678 -3.1; 1846 -2.7; 2031 -2.3; 2234 -2.3; 2457 -3.0; 2703 -4.3; 2973 -2.8; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.1; 4788 -7.9; 5267 -11.1; 5793 -4.8; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksoud RAIN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksoud RAIN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.24 | -6.0 dB |
| Peaking | 168 Hz  | 0.39 | -7.5 dB |
| Peaking | 1264 Hz | 0.52 | 4.5 dB  |
| Peaking | 3557 Hz | 4.16 | 5.3 dB  |
| Peaking | 4082 Hz | 7.94 | 2.4 dB  |
| Peaking | 5267 Hz | 4.59 | -8.2 dB |
| Peaking | 6254 Hz | 3.72 | 6.6 dB  |
| Peaking | 6442 Hz | 2.75 | 1.1 dB  |
| Peaking | 7578 Hz | 2.29 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksoud%20RAIN/Thinksoud%20RAIN.png)
# Focal Spirit One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.2; 25 -10.3; 28 -10.3; 31 -10.3; 34 -10.4; 37 -10.4; 41 -10.3; 45 -10.4; 49 -10.4; 54 -10.5; 60 -10.5; 66 -10.5; 72 -10.6; 79 -10.5; 87 -10.3; 96 -9.9; 106 -10.6; 116 -11.7; 128 -12.1; 141 -12.1; 155 -11.9; 170 -11.7; 187 -11.8; 206 -11.3; 227 -10.8; 249 -10.3; 274 -9.8; 302 -9.1; 332 -8.7; 365 -8.2; 402 -8.0; 442 -8.2; 486 -8.2; 535 -8.0; 588 -7.9; 647 -7.6; 712 -7.1; 783 -6.5; 861 -6.1; 947 -5.8; 1042 -5.4; 1146 -6.4; 1261 -6.3; 1387 -6.4; 1526 -6.8; 1678 -6.8; 1846 -6.2; 2031 -5.1; 2234 -3.8; 2457 -2.3; 2703 -1.1; 2973 -0.5; 3270 -0.6; 3597 -1.8; 3957 -3.9; 4353 -4.9; 4788 -4.8; 5267 -3.6; 5793 -0.6; 6373 -0.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.91 | -3.5 dB |
| Peaking | 49 Hz   | 1.19 | -2.1 dB |
| Peaking | 163 Hz  | 0.61 | -5.6 dB |
| Peaking | 3011 Hz | 2.48 | 6.1 dB  |
| Peaking | 6130 Hz | 4.65 | 6.1 dB  |
| Peaking | 588 Hz  | 3.45 | -0.9 dB |
| Peaking | 974 Hz  | 3.73 | 1.0 dB  |
| Peaking | 1672 Hz | 2.36 | -1.3 dB |
| Peaking | 2390 Hz | 4.86 | 1.1 dB  |
| Peaking | 8197 Hz | 4.81 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Focal%20Spirit%20One/Focal%20Spirit%20One.png)
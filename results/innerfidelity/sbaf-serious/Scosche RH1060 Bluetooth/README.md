# Scosche RH1060 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -8.0; 25 -8.6; 28 -9.4; 31 -10.0; 34 -10.5; 37 -10.8; 41 -11.2; 45 -11.5; 49 -11.8; 54 -12.0; 60 -12.3; 66 -12.5; 72 -12.7; 79 -12.8; 87 -13.0; 96 -13.1; 106 -13.1; 116 -13.0; 128 -12.9; 141 -12.8; 155 -13.0; 170 -12.1; 187 -11.7; 206 -11.5; 227 -10.8; 249 -10.5; 274 -9.2; 302 -7.7; 332 -6.7; 365 -4.7; 402 -2.8; 442 -1.4; 486 -0.9; 535 -0.7; 588 -0.5; 647 -1.4; 712 -2.8; 783 -3.5; 861 -4.2; 947 -4.8; 1042 -5.1; 1146 -4.9; 1261 -4.9; 1387 -5.3; 1526 -5.8; 1678 -6.6; 1846 -7.0; 2031 -6.8; 2234 -6.6; 2457 -6.8; 2703 -7.0; 2973 -7.1; 3270 -7.7; 3597 -7.2; 3957 -6.4; 4353 -5.8; 4788 -7.7; 5267 -6.2; 5793 -2.2; 6373 -1.3; 7010 -3.9; 7711 -6.2; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Scosche RH1060 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Scosche RH1060 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 302 Hz  | 0.12 | -3.7 dB |
| Peaking | 463 Hz  | 0.09 | -5.1 dB |
| Peaking | 495 Hz  | 1.13 | 9.2 dB  |
| Peaking | 1051 Hz | 0.35 | 7.6 dB  |
| Peaking | 6257 Hz | 4.12 | 6.5 dB  |
| Peaking | 123 Hz  | 4.82 | 0.2 dB  |
| Peaking | 1327 Hz | 3.12 | 1.9 dB  |
| Peaking | 1328 Hz | 1.68 | -1.3 dB |
| Peaking | 4302 Hz | 5.51 | 1.4 dB  |
| Peaking | 4897 Hz | 9.94 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 7.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Scosche%20RH1060%20Bluetooth/Scosche%20RH1060%20Bluetooth.png)
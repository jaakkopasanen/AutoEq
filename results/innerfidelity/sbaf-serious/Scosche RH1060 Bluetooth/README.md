# Scosche RH1060 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -8.0; 25 -8.6; 28 -9.4; 31 -10.0; 34 -10.5; 37 -10.8; 41 -11.2; 45 -11.5; 49 -11.8; 54 -12.0; 60 -12.3; 66 -12.5; 72 -12.7; 79 -12.8; 87 -13.0; 96 -13.1; 106 -13.1; 116 -13.0; 128 -12.9; 141 -12.8; 155 -13.1; 170 -12.1; 187 -11.7; 206 -11.5; 227 -10.8; 249 -10.5; 274 -9.2; 302 -7.7; 332 -6.7; 365 -4.7; 402 -2.8; 442 -1.4; 486 -0.9; 535 -0.7; 588 -0.5; 647 -1.4; 712 -2.8; 783 -3.5; 861 -4.2; 947 -4.8; 1042 -5.1; 1146 -4.9; 1261 -4.9; 1387 -5.3; 1526 -5.8; 1678 -6.6; 1846 -7.0; 2031 -6.8; 2234 -6.6; 2457 -6.8; 2703 -7.0; 2973 -7.1; 3270 -7.7; 3597 -7.2; 3957 -6.4; 4353 -5.8; 4788 -7.7; 5267 -6.2; 5793 -2.3; 6373 -0.7; 7010 -2.6; 7711 -5.6; 8482 -7.0; 9330 -5.2; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Scosche RH1060 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Scosche RH1060 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.42 | -5.9 dB |
| Peaking | 220 Hz  | 0.5  | -5.7 dB |
| Peaking | 492 Hz  | 1.12 | 8.5 dB  |
| Peaking | 3702 Hz | 0.46 | -2.4 dB |
| Peaking | 6376 Hz | 4.2  | 6.7 dB  |
| Peaking | 3332 Hz | 5.64 | -0.7 dB |
| Peaking | 4355 Hz | 3.66 | 1.3 dB  |
| Peaking | 4869 Hz | 8.28 | -2.7 dB |
| Peaking | 8370 Hz | 5.09 | -2.8 dB |
| Peaking | 8781 Hz | 1.08 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Scosche%20RH1060%20Bluetooth/Scosche%20RH1060%20Bluetooth.png)
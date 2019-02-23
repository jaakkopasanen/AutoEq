# Koss BT540i Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -11.2; 25 -11.6; 28 -12.1; 31 -12.5; 34 -12.8; 37 -13.0; 41 -13.2; 45 -13.3; 49 -13.4; 54 -13.4; 60 -13.5; 66 -13.5; 72 -13.5; 79 -13.5; 87 -13.5; 96 -13.5; 106 -13.2; 116 -13.0; 128 -12.8; 141 -12.8; 155 -12.9; 170 -12.0; 187 -11.7; 206 -11.9; 227 -11.3; 249 -10.5; 274 -9.6; 302 -8.2; 332 -7.8; 365 -6.7; 402 -5.5; 442 -4.4; 486 -3.8; 535 -3.2; 588 -2.7; 647 -3.0; 712 -3.7; 783 -4.0; 861 -4.4; 947 -4.5; 1042 -4.4; 1146 -4.6; 1261 -4.9; 1387 -5.5; 1526 -5.8; 1678 -6.5; 1846 -6.8; 2031 -7.1; 2234 -7.7; 2457 -8.2; 2703 -9.1; 2973 -9.6; 3270 -9.0; 3597 -7.3; 3957 -4.8; 4353 -2.8; 4788 -0.5; 5267 -1.3; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss BT540i Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.34 | -6.4 dB |
| Peaking | 271 Hz  | 0.53 | -5.8 dB |
| Peaking | 496 Hz  | 0.68 | 7.5 dB  |
| Peaking | 3049 Hz | 1.68 | -4.9 dB |
| Peaking | 5029 Hz | 1.71 | 7.2 dB  |
| Peaking | 846 Hz  | 4.14 | -0.5 dB |
| Peaking | 1123 Hz | 3.92 | 0.5 dB  |
| Peaking | 5580 Hz | 9.25 | -2.8 dB |
| Peaking | 6454 Hz | 2.92 | 4.1 dB  |
| Peaking | 7365 Hz | 2    | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Bluetooth/Koss%20BT540i%20Bluetooth.png)
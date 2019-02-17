# Parrot Zik2 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.8; 23 -17.4; 25 -16.9; 28 -16.0; 31 -15.2; 34 -14.4; 37 -13.8; 41 -13.1; 45 -12.5; 49 -12.0; 54 -11.5; 60 -10.9; 66 -10.3; 72 -9.9; 79 -9.3; 87 -8.9; 96 -8.4; 106 -7.8; 116 -7.2; 128 -6.9; 141 -6.5; 155 -6.3; 170 -6.0; 187 -5.7; 206 -5.3; 227 -5.0; 249 -4.9; 274 -4.7; 302 -4.5; 332 -4.2; 365 -3.9; 402 -3.9; 442 -3.6; 486 -3.5; 535 -3.5; 588 -3.2; 647 -3.0; 712 -3.2; 783 -3.6; 861 -4.8; 947 -5.9; 1042 -6.8; 1146 -7.3; 1261 -8.4; 1387 -9.4; 1526 -11.4; 1678 -13.8; 1846 -14.5; 2031 -13.9; 2234 -12.7; 2457 -11.0; 2703 -7.2; 2973 -4.4; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.1; 5267 -5.9; 5793 -4.8; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -11.1; 10263 -13.5; 11289 -11.9; 12418 -10.4; 13660 -9.0; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Parrot Zik2 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Parrot Zik2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.6  | -11.2 dB |
| Peaking | 63 Hz    | 0.9  | -1.3 dB  |
| Peaking | 1903 Hz  | 0.76 | -26.2 dB |
| Peaking | 2926 Hz  | 0.2  | 19.0 dB  |
| Peaking | 10516 Hz | 0.87 | -14.6 dB |
| Peaking | 717 Hz   | 1.95 | 2.0 dB   |
| Peaking | 1089 Hz  | 0.91 | -2.3 dB  |
| Peaking | 2484 Hz  | 3.29 | -5.3 dB  |
| Peaking | 2970 Hz  | 0.71 | 3.8 dB   |
| Peaking | 5267 Hz  | 4.91 | -6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB   |
| Peaking | 500 Hz   | 1.41 | 3.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.1 dB |
| Peaking | 4000 Hz  | 1.41 | 9.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Parrot%20Zik2%20Bluetooth/Parrot%20Zik2%20Bluetooth.png)
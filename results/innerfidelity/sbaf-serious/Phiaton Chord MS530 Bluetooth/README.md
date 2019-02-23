# Phiaton Chord MS530 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.8; 25 -8.3; 28 -8.8; 31 -9.3; 34 -9.6; 37 -9.9; 41 -10.2; 45 -10.5; 49 -10.7; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.5; 79 -11.6; 87 -11.7; 96 -11.8; 106 -11.6; 116 -11.3; 128 -11.2; 141 -10.5; 155 -10.1; 170 -9.7; 187 -8.9; 206 -9.1; 227 -8.9; 249 -8.6; 274 -8.0; 302 -7.6; 332 -7.4; 365 -7.4; 402 -7.5; 442 -7.6; 486 -7.9; 535 -8.2; 588 -8.0; 647 -8.2; 712 -8.7; 783 -8.9; 861 -9.5; 947 -10.3; 1042 -11.3; 1146 -11.9; 1261 -12.4; 1387 -13.2; 1526 -12.3; 1678 -12.0; 1846 -13.3; 2031 -11.9; 2234 -10.4; 2457 -8.5; 2703 -6.5; 2973 -4.6; 3270 -2.5; 3597 -2.2; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Chord MS530 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 1.1  | 1.0 dB  |
| Peaking | 42 Hz   | 0.71 | -2.7 dB |
| Peaking | 104 Hz  | 0.75 | -4.3 dB |
| Peaking | 1624 Hz | 0.87 | -7.8 dB |
| Peaking | 4310 Hz | 1.09 | 8.2 dB  |
| Peaking | 1613 Hz | 9.53 | 4.8 dB  |
| Peaking | 1686 Hz | 3.25 | -2.1 dB |
| Peaking | 3141 Hz | 6.07 | 1.9 dB  |
| Peaking | 6234 Hz | 2.71 | 6.3 dB  |
| Peaking | 6757 Hz | 1.27 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530%20Bluetooth/Phiaton%20Chord%20MS530%20Bluetooth.png)
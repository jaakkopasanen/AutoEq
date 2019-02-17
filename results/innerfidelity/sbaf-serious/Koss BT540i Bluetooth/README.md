# Koss BT540i Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.9; 25 -13.3; 28 -13.8; 31 -14.2; 34 -14.4; 37 -14.7; 41 -14.9; 45 -15.0; 49 -15.1; 54 -15.1; 60 -15.2; 66 -15.1; 72 -15.2; 79 -15.2; 87 -15.2; 96 -15.2; 106 -14.9; 116 -14.7; 128 -14.5; 141 -14.5; 155 -14.6; 170 -13.6; 187 -13.4; 206 -13.5; 227 -13.0; 249 -12.2; 274 -11.3; 302 -9.9; 332 -9.5; 365 -8.4; 402 -7.1; 442 -6.1; 486 -5.5; 535 -4.8; 588 -4.3; 647 -4.7; 712 -5.4; 783 -5.7; 861 -6.1; 947 -6.2; 1042 -6.0; 1146 -6.3; 1261 -6.6; 1387 -7.1; 1526 -7.4; 1678 -8.1; 1846 -8.5; 2031 -8.8; 2234 -9.4; 2457 -9.9; 2703 -10.8; 2973 -11.3; 3270 -10.7; 3597 -9.0; 3957 -6.5; 4353 -4.5; 4788 -0.5; 5267 -2.4; 5793 -3.2; 6373 -2.0; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -7.4; 10263 -6.2; 11289 -6.2; 12418 -6.5; 13660 -7.0; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss BT540i Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 36 Hz    |  0.41 | -6.8 dB |
| Peaking | 186 Hz   |  0.37 | -7.2 dB |
| Peaking | 521 Hz   |  0.91 | 5.5 dB  |
| Peaking | 3268 Hz  |  1.06 | -7.4 dB |
| Peaking | 4852 Hz  |  1.67 | 8.8 dB  |
| Peaking | 1127 Hz  |  6.9  | 0.5 dB  |
| Peaking | 5534 Hz  | 14.63 | -2.7 dB |
| Peaking | 6524 Hz  |  6.46 | 2.5 dB  |
| Peaking | 9068 Hz  |  4.28 | -1.5 dB |
| Peaking | 13241 Hz |  6.45 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.7 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Bluetooth/Koss%20BT540i%20Bluetooth.png)
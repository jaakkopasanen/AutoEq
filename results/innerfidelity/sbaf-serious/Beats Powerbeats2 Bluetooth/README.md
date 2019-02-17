# Beats Powerbeats2 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.2; 25 -7.3; 28 -7.4; 31 -7.5; 34 -7.6; 37 -7.7; 41 -7.9; 45 -8.0; 49 -8.1; 54 -8.2; 60 -8.4; 66 -8.5; 72 -8.8; 79 -9.0; 87 -9.4; 96 -9.7; 106 -10.0; 116 -10.1; 128 -10.4; 141 -10.7; 155 -10.9; 170 -10.8; 187 -10.9; 206 -11.0; 227 -10.8; 249 -10.8; 274 -10.6; 302 -10.5; 332 -10.3; 365 -10.1; 402 -9.8; 442 -9.4; 486 -9.3; 535 -8.8; 588 -8.2; 647 -7.8; 712 -7.5; 783 -6.9; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -6.3; 1261 -6.1; 1387 -6.2; 1526 -6.2; 1678 -6.2; 1846 -5.8; 2031 -5.2; 2234 -4.3; 2457 -2.8; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.7; 4788 -3.2; 5267 -3.2; 5793 -3.2; 6373 -4.3; 7010 -6.1; 7711 -8.0; 8482 -9.0; 9330 -8.2; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -9.5; 16529 -10.4; 18182 -9.8; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats2 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 78 Hz    | 0.33 | -1.2 dB |
| Peaking | 160 Hz   | 0.75 | -2.8 dB |
| Peaking | 354 Hz   | 0.9  | -2.4 dB |
| Peaking | 3491 Hz  | 1.33 | 6.8 dB  |
| Peaking | 18541 Hz | 0.47 | -3.9 dB |
| Peaking | 1862 Hz  | 3.09 | -0.9 dB |
| Peaking | 2720 Hz  | 6.81 | 1.2 dB  |
| Peaking | 5979 Hz  | 4.32 | 1.8 dB  |
| Peaking | 8366 Hz  | 3.19 | -3.2 dB |
| Peaking | 12327 Hz | 2.29 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Powerbeats2%20Bluetooth/Beats%20Powerbeats2%20Bluetooth.png)
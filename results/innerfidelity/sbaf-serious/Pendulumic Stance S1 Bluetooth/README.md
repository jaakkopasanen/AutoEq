# Pendulumic Stance S1 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.8; 49 -3.1; 54 -4.5; 60 -5.9; 66 -7.0; 72 -8.0; 79 -8.7; 87 -9.4; 96 -10.1; 106 -10.3; 116 -10.3; 128 -10.4; 141 -10.4; 155 -10.3; 170 -10.1; 187 -9.8; 206 -9.8; 227 -9.6; 249 -9.5; 274 -9.3; 302 -9.2; 332 -9.5; 365 -9.1; 402 -8.9; 442 -8.4; 486 -7.7; 535 -7.0; 588 -6.0; 647 -5.7; 712 -6.1; 783 -6.7; 861 -7.2; 947 -6.6; 1042 -6.8; 1146 -7.5; 1261 -8.8; 1387 -8.8; 1526 -8.6; 1678 -9.2; 1846 -8.3; 2031 -6.3; 2234 -4.2; 2457 -2.6; 2703 -1.9; 2973 -3.4; 3270 -2.7; 3597 -0.5; 3957 -2.8; 4353 -5.2; 4788 -4.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -7.7; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pendulumic Stance S1 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pendulumic Stance S1 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.56 | 11.4 dB |
| Peaking | 82 Hz    | 0.36 | -7.6 dB |
| Peaking | 3339 Hz  | 2.27 | 4.9 dB  |
| Peaking | 5833 Hz  | 3.63 | 6.3 dB  |
| Peaking | 22050 Hz | 2.43 | 4.2 dB  |
| Peaking | 392 Hz   | 2.74 | -1.0 dB |
| Peaking | 631 Hz   | 2.51 | 1.9 dB  |
| Peaking | 1627 Hz  | 1.69 | -3.1 dB |
| Peaking | 2428 Hz  | 4.28 | 3.6 dB  |
| Peaking | 8976 Hz  | 4.6  | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pendulumic%20Stance%20S1%20Bluetooth/Pendulumic%20Stance%20S1%20Bluetooth.png)
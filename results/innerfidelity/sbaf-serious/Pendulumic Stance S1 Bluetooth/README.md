# Pendulumic Stance S1 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.7; 49 -3.0; 54 -4.4; 60 -5.8; 66 -6.9; 72 -7.9; 79 -8.6; 87 -9.3; 96 -10.0; 106 -10.2; 116 -10.2; 128 -10.3; 141 -10.3; 155 -10.2; 170 -10.0; 187 -9.7; 206 -9.7; 227 -9.5; 249 -9.4; 274 -9.2; 302 -9.1; 332 -9.4; 365 -9.0; 402 -8.8; 442 -8.3; 486 -7.6; 535 -6.9; 588 -5.9; 647 -5.6; 712 -6.0; 783 -6.6; 861 -7.1; 947 -6.5; 1042 -6.7; 1146 -7.4; 1261 -8.7; 1387 -8.7; 1526 -8.5; 1678 -9.1; 1846 -8.2; 2031 -6.2; 2234 -4.1; 2457 -2.5; 2703 -1.8; 2973 -3.3; 3270 -2.6; 3597 -0.5; 3957 -2.7; 4353 -5.1; 4788 -4.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -7.6; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pendulumic Stance S1 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pendulumic Stance S1 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.54 | 11.6 dB |
| Peaking | 81 Hz    | 0.38 | -8.0 dB |
| Peaking | 3321 Hz  | 2.19 | 4.9 dB  |
| Peaking | 5830 Hz  | 3.59 | 6.3 dB  |
| Peaking | 22050 Hz | 2.43 | 4.2 dB  |
| Peaking | 392 Hz   | 2.69 | -1.1 dB |
| Peaking | 632 Hz   | 2.41 | 1.9 dB  |
| Peaking | 1628 Hz  | 1.72 | -3.1 dB |
| Peaking | 2411 Hz  | 4.31 | 3.5 dB  |
| Peaking | 9020 Hz  | 4.5  | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pendulumic%20Stance%20S1%20Bluetooth/Pendulumic%20Stance%20S1%20Bluetooth.png)
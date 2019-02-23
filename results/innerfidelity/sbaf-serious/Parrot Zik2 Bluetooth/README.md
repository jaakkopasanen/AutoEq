# Parrot Zik2 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.0; 23 -18.6; 25 -18.1; 28 -17.3; 31 -16.4; 34 -15.7; 37 -15.0; 41 -14.3; 45 -13.7; 49 -13.2; 54 -12.7; 60 -12.1; 66 -11.6; 72 -11.1; 79 -10.6; 87 -10.1; 96 -9.6; 106 -9.0; 116 -8.5; 128 -8.1; 141 -7.7; 155 -7.5; 170 -7.3; 187 -6.9; 206 -6.6; 227 -6.3; 249 -6.2; 274 -5.9; 302 -5.7; 332 -5.4; 365 -5.1; 402 -5.1; 442 -4.8; 486 -4.7; 535 -4.7; 588 -4.4; 647 -4.2; 712 -4.4; 783 -4.8; 861 -6.0; 947 -7.1; 1042 -8.1; 1146 -8.5; 1261 -9.7; 1387 -10.7; 1526 -12.7; 1678 -15.0; 1846 -15.7; 2031 -15.1; 2234 -14.0; 2457 -12.2; 2703 -8.4; 2973 -5.6; 3270 -0.9; 3597 -1.6; 3957 -1.3; 4353 -0.5; 4788 -2.9; 5267 -7.1; 5793 -6.0; 6373 -3.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -12.3; 10263 -14.7; 11289 -13.1; 12418 -11.6; 13660 -10.2; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Parrot Zik2 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Parrot Zik2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.79 | -12.1 dB |
| Peaking | 62 Hz    | 1.16 | -2.7 dB  |
| Peaking | 1988 Hz  | 1.79 | -11.6 dB |
| Peaking | 3724 Hz  | 1.49 | 7.8 dB   |
| Peaking | 10818 Hz | 2.27 | -8.8 dB  |
| Peaking | 422 Hz   | 1.35 | 1.7 dB   |
| Peaking | 692 Hz   | 2.57 | 2.4 dB   |
| Peaking | 1552 Hz  | 3.88 | -1.4 dB  |
| Peaking | 5245 Hz  | 9.01 | -3.9 dB  |
| Peaking | 6808 Hz  | 5.39 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB   |
| Peaking | 500 Hz   | 1.41 | 2.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Parrot%20Zik2%20Bluetooth/Parrot%20Zik2%20Bluetooth.png)
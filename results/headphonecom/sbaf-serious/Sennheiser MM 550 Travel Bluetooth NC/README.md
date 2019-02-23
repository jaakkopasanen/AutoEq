# Sennheiser MM 550 Travel Bluetooth NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.3; 60 -1.9; 66 -2.5; 72 -2.9; 79 -3.4; 87 -3.9; 96 -4.4; 106 -4.3; 116 -4.1; 128 -4.6; 141 -3.3; 155 -3.4; 170 -3.4; 187 -3.0; 206 -3.8; 227 -4.6; 249 -5.4; 274 -6.2; 302 -7.4; 332 -9.0; 365 -10.2; 402 -9.9; 442 -9.6; 486 -9.0; 535 -8.1; 588 -7.6; 647 -7.1; 712 -6.6; 783 -6.6; 861 -6.6; 947 -6.8; 1042 -7.4; 1146 -8.5; 1261 -10.1; 1387 -12.3; 1526 -14.8; 1678 -16.5; 1846 -17.4; 2031 -16.4; 2234 -14.1; 2457 -11.0; 2703 -8.3; 2973 -6.2; 3270 -4.5; 3597 -2.1; 3957 -0.5; 4353 -2.5; 4788 -5.8; 5267 -4.5; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -9.5; 11289 -9.4; 12418 -6.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550 Travel Bluetooth NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550 Travel Bluetooth NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.08 | 5.4 dB   |
| Peaking | 392 Hz   | 2.64 | -4.6 dB  |
| Peaking | 1844 Hz  | 2.02 | -12.0 dB |
| Peaking | 3811 Hz  | 3.2  | 7.2 dB   |
| Peaking | 6128 Hz  | 5.14 | 6.4 dB   |
| Peaking | 97 Hz    | 2.28 | -1.8 dB  |
| Peaking | 186 Hz   | 3.86 | 1.8 dB   |
| Peaking | 938 Hz   | 2.78 | 1.4 dB   |
| Peaking | 1474 Hz  | 6.59 | -1.5 dB  |
| Peaking | 10714 Hz | 3.96 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB   |
| Peaking | 62 Hz    | 1.41 | 2.6 dB   |
| Peaking | 125 Hz   | 1.41 | 2.2 dB   |
| Peaking | 250 Hz   | 1.41 | 1.0 dB   |
| Peaking | 500 Hz   | 1.41 | -3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -12.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MM%20550%20Travel%20Bluetooth%20NC/Sennheiser%20MM%20550%20Travel%20Bluetooth%20NC.png)
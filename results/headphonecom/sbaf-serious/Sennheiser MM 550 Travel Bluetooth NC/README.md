# Sennheiser MM 550 Travel Bluetooth NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.4; 66 -1.9; 72 -2.3; 79 -2.8; 87 -3.3; 96 -3.8; 106 -3.7; 116 -3.5; 128 -4.0; 141 -2.7; 155 -2.8; 170 -2.8; 187 -2.5; 206 -3.2; 227 -4.1; 249 -4.9; 274 -5.7; 302 -6.8; 332 -8.5; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.4; 535 -7.6; 588 -7.1; 647 -6.5; 712 -6.0; 783 -6.0; 861 -6.0; 947 -6.3; 1042 -6.9; 1146 -8.0; 1261 -9.6; 1387 -11.7; 1526 -14.3; 1678 -16.0; 1846 -16.8; 2031 -15.9; 2234 -13.5; 2457 -10.5; 2703 -7.7; 2973 -5.7; 3270 -3.9; 3597 -1.5; 3957 -0.5; 4353 -1.9; 4788 -5.2; 5267 -3.9; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -8.9; 11289 -8.8; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550 Travel Bluetooth NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550 Travel Bluetooth NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.48 | 6.5 dB   |
| Peaking | 177 Hz   | 2.7  | 3.4 dB   |
| Peaking | 1848 Hz  | 2.06 | -11.5 dB |
| Peaking | 3769 Hz  | 2.81 | 7.2 dB   |
| Peaking | 6151 Hz  | 4.9  | 6.2 dB   |
| Peaking | 276 Hz   | 1.46 | 2.5 dB   |
| Peaking | 370 Hz   | 1.57 | -5.0 dB  |
| Peaking | 875 Hz   | 1.29 | 2.0 dB   |
| Peaking | 1460 Hz  | 4.84 | -1.7 dB  |
| Peaking | 10685 Hz | 4.03 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 3.2 dB   |
| Peaking | 125 Hz   | 1.41 | 2.6 dB   |
| Peaking | 250 Hz   | 1.41 | 1.4 dB   |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -12.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MM%20550%20Travel%20Bluetooth%20NC/Sennheiser%20MM%20550%20Travel%20Bluetooth%20NC.png)
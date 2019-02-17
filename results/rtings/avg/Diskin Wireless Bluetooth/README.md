# Diskin Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -4.5; 25 -6.4; 28 -8.9; 31 -10.5; 34 -11.1; 37 -11.1; 41 -10.4; 45 -9.8; 49 -9.2; 54 -8.6; 60 -8.2; 66 -8.1; 72 -8.0; 79 -8.0; 87 -8.1; 96 -8.3; 106 -8.5; 116 -8.7; 128 -8.9; 141 -9.1; 155 -9.2; 170 -9.2; 187 -9.2; 206 -9.0; 227 -8.9; 249 -8.9; 274 -8.9; 302 -8.8; 332 -8.5; 365 -8.0; 402 -7.6; 442 -6.4; 486 -4.8; 535 -3.9; 588 -3.5; 647 -3.5; 712 -3.9; 783 -4.4; 861 -5.1; 947 -5.9; 1042 -6.9; 1146 -7.6; 1261 -8.6; 1387 -9.7; 1526 -10.5; 1678 -10.3; 1846 -9.1; 2031 -7.7; 2234 -6.4; 2457 -4.7; 2703 -3.8; 2973 -4.3; 3270 -5.0; 3597 -4.8; 3957 -4.1; 4353 -3.2; 4788 -1.0; 5267 -0.5; 5793 -0.9; 6373 -2.6; 7010 -5.1; 7711 -6.7; 8482 -7.6; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Diskin Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Diskin Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 2.37 | -4.6 dB |
| Peaking | 241 Hz  | 0.43 | -3.1 dB |
| Peaking | 609 Hz  | 1.47 | 5.1 dB  |
| Peaking | 1541 Hz | 2.95 | -4.8 dB |
| Peaking | 5152 Hz | 2.06 | 6.3 dB  |
| Peaking | 52 Hz   | 3.29 | -0.3 dB |
| Peaking | 1875 Hz | 4.8  | -0.9 dB |
| Peaking | 2670 Hz | 4.32 | 2.7 dB  |
| Peaking | 6200 Hz | 6.1  | 1.6 dB  |
| Peaking | 8165 Hz | 2.51 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Diskin%20Wireless%20Bluetooth/Diskin%20Wireless%20Bluetooth.png)
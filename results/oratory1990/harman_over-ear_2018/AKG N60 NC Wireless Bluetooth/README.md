# AKG N60 NC Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.6; 41 -2.6; 45 -3.4; 49 -4.2; 54 -5.1; 60 -6.0; 66 -6.9; 72 -7.5; 79 -8.1; 87 -8.6; 96 -9.1; 106 -9.4; 116 -9.7; 128 -9.9; 141 -9.9; 155 -9.9; 170 -9.7; 187 -9.5; 206 -9.2; 227 -9.0; 249 -8.7; 274 -8.1; 302 -7.5; 332 -6.8; 365 -6.5; 402 -6.3; 442 -5.7; 486 -5.2; 535 -5.0; 588 -5.0; 647 -5.1; 712 -5.3; 783 -5.4; 861 -5.7; 947 -6.3; 1042 -6.6; 1146 -6.6; 1261 -6.5; 1387 -6.1; 1526 -5.5; 1678 -5.2; 1846 -5.0; 2031 -5.1; 2234 -5.7; 2457 -6.6; 2703 -7.9; 2973 -9.8; 3270 -11.6; 3597 -13.0; 3957 -12.7; 4353 -10.2; 4788 -9.6; 5267 -13.8; 5793 -13.0; 6373 -7.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -9.4; 18182 -11.8; 20000 -13.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N60 NC Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60 NC Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.76 | 6.9 dB  |
| Peaking | 136 Hz  |  0.61 | -4.8 dB |
| Peaking | 1110 Hz |  0.13 | 1.5 dB  |
| Peaking | 3637 Hz |  2.49 | -7.9 dB |
| Peaking | 5432 Hz |  5.73 | -8.1 dB |
| Peaking | 246 Hz  |  4.02 | -0.6 dB |
| Peaking | 553 Hz  |  1.87 | 1.0 dB  |
| Peaking | 1122 Hz |  2.12 | -1.6 dB |
| Peaking | 1929 Hz |  3.59 | 1.1 dB  |
| Peaking | 6921 Hz | 12.39 | 3.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20N60%20NC%20Wireless%20Bluetooth/AKG%20N60%20NC%20Wireless%20Bluetooth.png)
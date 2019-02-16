# AKG N60NC Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.5dB
GraphicEQ: 21 -1.8; 23 -2.2; 25 -2.7; 28 -3.3; 31 -3.8; 34 -4.2; 37 -4.5; 41 -4.8; 45 -5.2; 49 -5.4; 54 -5.8; 60 -6.1; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.6; 96 -7.9; 106 -8.1; 116 -8.4; 128 -8.5; 141 -8.6; 155 -8.6; 170 -8.5; 187 -8.3; 206 -8.2; 227 -8.0; 249 -7.8; 274 -7.6; 302 -7.5; 332 -7.5; 365 -7.3; 402 -6.8; 442 -6.5; 486 -6.2; 535 -5.9; 588 -5.4; 647 -4.7; 712 -3.7; 783 -2.9; 861 -2.2; 947 -1.7; 1042 -1.4; 1146 -1.2; 1261 -1.3; 1387 -1.1; 1526 -0.5; 1678 -1.1; 1846 -1.4; 2031 -1.7; 2234 -1.7; 2457 -1.8; 2703 -3.1; 2973 -5.6; 3270 -8.1; 3597 -9.4; 3957 -8.1; 4353 -5.7; 4788 -4.2; 5267 -5.5; 5793 -8.5; 6373 -10.8; 7010 -7.4; 7711 -4.6; 8482 -5.5; 9330 -6.9; 10263 -3.8; 11289 -1.5; 12418 -1.5; 13660 -1.6; 15026 -3.8; 16529 -4.5; 18182 -2.3; 20000 -1.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N60NC Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-14**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 127 Hz   | 0.43 | -6.9 dB |
| Peaking | 405 Hz   | 1.27 | -3.0 dB |
| Peaking | 3549 Hz  | 3.77 | -7.7 dB |
| Peaking | 6421 Hz  | 2.3  | -8.2 dB |
| Peaking | 16332 Hz | 2.09 | -3.3 dB |
| Peaking | 1033 Hz  | 4.15 | 1.0 dB  |
| Peaking | 1565 Hz  | 2.28 | 1.4 dB  |
| Peaking | 7651 Hz  | 5.53 | 2.3 dB  |
| Peaking | 9438 Hz  | 3.35 | -5.2 dB |
| Peaking | 10924 Hz | 2.13 | 2.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N60NC%20Wireless/AKG%20N60NC%20Wireless.png)
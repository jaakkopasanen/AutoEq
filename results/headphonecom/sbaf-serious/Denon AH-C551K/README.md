# Denon AH-C551K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.9; 28 -11.0; 31 -11.1; 34 -11.1; 37 -11.1; 41 -11.1; 45 -11.2; 49 -11.2; 54 -11.2; 60 -11.4; 66 -11.6; 72 -11.7; 79 -11.6; 87 -11.6; 96 -11.6; 106 -11.4; 116 -11.2; 128 -10.9; 141 -10.6; 155 -10.2; 170 -9.5; 187 -10.0; 206 -9.8; 227 -9.1; 249 -8.3; 274 -7.6; 302 -6.8; 332 -5.9; 365 -5.0; 402 -4.2; 442 -3.4; 486 -2.7; 535 -1.9; 588 -1.1; 647 -0.5; 712 0.0; 783 0.5; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.0; 1526 -3.6; 1678 -4.9; 1846 -6.0; 2031 -6.8; 2234 -7.8; 2457 -9.3; 2703 -11.3; 2973 -11.2; 3270 -7.1; 3597 -4.1; 3957 -4.2; 4353 -6.4; 4788 -8.8; 5267 -11.5; 5793 -12.4; 6373 -8.5; 7010 -7.0; 7711 -9.1; 8482 -11.3; 9330 -7.3; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.6; 16529 -0.2; 18182 0.0; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C551K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.26 | -11.4 dB |
| Peaking | 195 Hz   | 0.84 | -4.9 dB  |
| Peaking | 2564 Hz  | 2.02 | -9.4 dB  |
| Peaking | 6257 Hz  | 1.17 | -10.3 dB |
| Peaking | 24000 Hz | 2.11 | -8.7 dB  |
| Peaking | 3927 Hz  | 3.65 | 5.1 dB   |
| Peaking | 5931 Hz  | 1.03 | -4.8 dB  |
| Peaking | 6750 Hz  | 3.54 | 8.1 dB   |
| Peaking | 8706 Hz  | 3.53 | -8.0 dB  |
| Peaking | 10388 Hz | 2.18 | 6.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C551K/Denon%20AH-C551K.png)
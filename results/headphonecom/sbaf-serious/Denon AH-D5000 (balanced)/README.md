# Denon AH-D5000 (balanced)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.7; 28 -0.1; 31 -0.5; 34 -0.7; 37 -0.9; 41 -1.1; 45 -1.2; 49 -1.0; 54 -0.9; 60 -1.1; 66 -1.2; 72 -1.4; 79 -1.6; 87 -1.9; 96 -1.9; 106 -2.0; 116 -2.2; 128 -2.2; 141 -2.1; 155 -2.1; 170 -2.1; 187 -2.1; 206 -2.2; 227 -2.0; 249 -1.9; 274 -1.6; 302 -1.5; 332 -1.2; 365 -0.9; 402 -0.5; 442 -0.2; 486 0.2; 535 0.8; 588 1.5; 647 1.8; 712 0.8; 783 -1.0; 861 -1.2; 947 1.3; 1042 -0.5; 1146 -1.2; 1261 -1.8; 1387 -2.5; 1526 -3.0; 1678 -3.5; 1846 -3.5; 2031 -3.2; 2234 -3.2; 2457 -1.9; 2703 1.5; 2973 1.8; 3270 1.1; 3597 0.2; 3957 -1.4; 4353 -2.7; 4788 -2.7; 5267 -1.4; 5793 0.4; 6373 -2.0; 7010 -4.0; 7711 -4.2; 8482 -3.6; 9330 -4.2; 10263 -1.2; 11289 0.0; 12418 -0.7; 13660 -2.1; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 (balanced) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 2.85 | 2.4 dB  |
| Peaking | 129 Hz   | 0.6  | -2.4 dB |
| Peaking | 1754 Hz  | 2.35 | -4.0 dB |
| Peaking | 7971 Hz  | 1.98 | -4.4 dB |
| Peaking | 13531 Hz | 3.44 | -1.0 dB |
| Peaking | 614 Hz   | 4.54 | 2.4 dB  |
| Peaking | 2358 Hz  | 4.19 | -3.5 dB |
| Peaking | 2820 Hz  | 2.59 | 4.0 dB  |
| Peaking | 4532 Hz  | 3.06 | -2.8 dB |
| Peaking | 5796 Hz  | 8.22 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D5000%20(balanced)/Denon%20AH-D5000%20(balanced).png)
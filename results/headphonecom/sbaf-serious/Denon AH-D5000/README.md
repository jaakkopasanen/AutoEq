# Denon AH-D5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.8; 28 0.2; 31 -0.1; 34 -0.4; 37 -0.7; 41 -0.9; 45 -0.7; 49 -0.7; 54 -0.9; 60 -1.0; 66 -1.2; 72 -1.4; 79 -1.6; 87 -1.8; 96 -2.1; 106 -2.0; 116 -2.2; 128 -2.4; 141 -2.5; 155 -2.6; 170 -2.5; 187 -2.3; 206 -2.2; 227 -2.1; 249 -2.1; 274 -2.1; 302 -1.9; 332 -1.6; 365 -1.2; 402 -0.8; 442 -0.4; 486 0.0; 535 0.6; 588 1.4; 647 1.5; 712 0.3; 783 -1.7; 861 -0.9; 947 1.1; 1042 -0.6; 1146 -1.3; 1261 -1.9; 1387 -2.5; 1526 -3.2; 1678 -3.7; 1846 -3.7; 2031 -3.3; 2234 -2.6; 2457 -1.4; 2703 1.1; 2973 1.1; 3270 0.5; 3597 -0.5; 3957 -2.1; 4353 -3.8; 4788 -3.2; 5267 -1.7; 5793 -0.3; 6373 -2.0; 7010 -4.3; 7711 -3.9; 8482 -3.6; 9330 -5.2; 10263 -1.0; 11289 0.0; 12418 -0.0; 13660 -0.9; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 2.63 | 2.6 dB  |
| Peaking | 146 Hz   | 0.65 | -2.6 dB |
| Peaking | 1731 Hz  | 2.33 | -4.0 dB |
| Peaking | 7938 Hz  | 1.58 | -4.3 dB |
| Peaking | 19902 Hz | 4.24 | -7.2 dB |
| Peaking | 18 Hz    | 1.87 | 0.9 dB  |
| Peaking | 606 Hz   | 5.06 | 2.3 dB  |
| Peaking | 2915 Hz  | 5.63 | 2.5 dB  |
| Peaking | 4400 Hz  | 5.69 | -3.5 dB |
| Peaking | 13820 Hz | 0.37 | 0.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)
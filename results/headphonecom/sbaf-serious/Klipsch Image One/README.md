# Klipsch Image One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 4.7; 28 3.7; 31 2.9; 34 2.1; 37 1.5; 41 0.8; 45 0.1; 49 -0.4; 54 -1.0; 60 -1.5; 66 -1.9; 72 -2.2; 79 -2.7; 87 -3.2; 96 -3.6; 106 -3.8; 116 -4.2; 128 -4.2; 141 -4.5; 155 -4.7; 170 -4.6; 187 -4.8; 206 -4.5; 227 -4.1; 249 -3.7; 274 -3.4; 302 -3.3; 332 -3.0; 365 -2.5; 402 -2.3; 442 -2.3; 486 -1.8; 535 -1.0; 588 0.1; 647 1.2; 712 1.6; 783 1.1; 861 0.3; 947 -0.5; 1042 0.2; 1146 -1.4; 1261 -2.0; 1387 -2.8; 1526 -3.2; 1678 -3.9; 1846 -4.6; 2031 -5.1; 2234 -5.3; 2457 -5.9; 2703 -6.8; 2973 -6.5; 3270 -5.0; 3597 -2.4; 3957 0.5; 4353 1.5; 4788 1.3; 5267 1.1; 5793 0.1; 6373 0.3; 7010 -0.7; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-70**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.1  | 6.9 dB  |
| Peaking | 114 Hz  | 0.74 | -3.7 dB |
| Peaking | 231 Hz  | 1.15 | -2.7 dB |
| Peaking | 2791 Hz | 1.15 | -8.2 dB |
| Peaking | 4287 Hz | 1.92 | 5.4 dB  |
| Peaking | 171 Hz  | 4.55 | -0.3 dB |
| Peaking | 479 Hz  | 1.81 | -2.2 dB |
| Peaking | 679 Hz  | 1.49 | 3.2 dB  |
| Peaking | 1638 Hz | 1.45 | -1.3 dB |
| Peaking | 2375 Hz | 5.03 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)
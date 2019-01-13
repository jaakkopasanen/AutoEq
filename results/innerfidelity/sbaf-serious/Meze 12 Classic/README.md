# Meze 12 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 0.3; 25 -0.2; 28 -0.7; 31 -1.2; 34 -1.6; 37 -2.0; 41 -2.5; 45 -2.8; 49 -3.2; 54 -3.6; 60 -4.1; 66 -4.4; 72 -4.9; 79 -5.3; 87 -5.8; 96 -6.1; 106 -6.4; 116 -6.5; 128 -6.7; 141 -6.8; 155 -6.9; 170 -6.8; 187 -6.7; 206 -6.5; 227 -6.2; 249 -5.9; 274 -5.4; 302 -5.0; 332 -4.5; 365 -3.9; 402 -3.3; 442 -2.7; 486 -2.2; 535 -1.6; 588 -0.8; 647 -0.3; 712 0.3; 783 0.5; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.3; 1678 -3.0; 1846 -3.5; 2031 -3.9; 2234 -4.3; 2457 -3.8; 2703 -2.4; 2973 0.0; 3270 2.4; 3597 3.4; 3957 2.7; 4353 0.6; 4788 -0.1; 5267 1.0; 5793 2.4; 6373 4.6; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 12 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 12 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.54 | -4.9 dB |
| Peaking | 278 Hz  | 0.56 | -4.5 dB |
| Peaking | 1799 Hz | 0.27 | 5.0 dB  |
| Peaking | 2130 Hz | 0.86 | -9.2 dB |
| Peaking | 3450 Hz | 3.82 | 4.5 dB  |
| Peaking | 17 Hz   | 2.11 | 1.6 dB  |
| Peaking | 1138 Hz | 5.88 | -0.2 dB |
| Peaking | 4751 Hz | 7.64 | -1.6 dB |
| Peaking | 6457 Hz | 4.94 | 4.6 dB  |
| Peaking | 8139 Hz | 1.44 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2012%20Classic/Meze%2012%20Classic.png)
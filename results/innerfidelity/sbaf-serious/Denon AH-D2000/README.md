# Denon AH-D2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 5.6; 49 5.5; 54 5.5; 60 5.6; 66 5.3; 72 5.0; 79 4.8; 87 4.6; 96 4.3; 106 4.2; 116 4.1; 128 3.8; 141 3.6; 155 3.5; 170 3.5; 187 3.6; 206 3.4; 227 3.4; 249 3.4; 274 3.3; 302 3.3; 332 3.1; 365 2.9; 402 2.6; 442 2.2; 486 1.5; 535 0.9; 588 0.7; 647 0.3; 712 -0.2; 783 1.4; 861 0.2; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.6; 1387 0.6; 1526 0.6; 1678 0.9; 1846 1.2; 2031 1.8; 2234 2.2; 2457 2.8; 2703 3.2; 2973 5.4; 3270 5.2; 3597 2.7; 3957 2.1; 4353 2.2; 4788 2.7; 5267 3.2; 5793 2.2; 6373 1.3; 7010 1.0; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.17 | 6.0 dB  |
| Peaking | 284 Hz  | 2.92 | -1.3 dB |
| Peaking | 291 Hz  | 1.4  | 3.3 dB  |
| Peaking | 3025 Hz | 2.27 | 5.0 dB  |
| Peaking | 5311 Hz | 3.33 | 2.6 dB  |
| Peaking | 675 Hz  | 7.43 | -0.8 dB |
| Peaking | 2042 Hz | 6.45 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)
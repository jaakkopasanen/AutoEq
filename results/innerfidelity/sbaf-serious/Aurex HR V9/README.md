# Aurex HR V9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.5; 54 5.1; 60 4.8; 66 4.5; 72 4.2; 79 3.9; 87 3.5; 96 3.4; 106 2.7; 116 2.3; 128 2.0; 141 1.7; 155 1.6; 170 1.5; 187 1.3; 206 1.3; 227 1.3; 249 1.2; 274 1.4; 302 1.4; 332 1.4; 365 1.3; 402 1.3; 442 1.4; 486 1.2; 535 1.1; 588 1.4; 647 1.3; 712 1.0; 783 0.9; 861 0.2; 947 -0.1; 1042 0.1; 1146 0.3; 1261 1.1; 1387 1.5; 1526 2.2; 1678 2.7; 1846 2.9; 2031 1.3; 2234 0.1; 2457 0.8; 2703 1.8; 2973 3.1; 3270 3.8; 3597 4.3; 3957 4.3; 4353 3.5; 4788 3.7; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aurex HR V9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurex HR V9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.31 | 6.1 dB  |
| Peaking | 143 Hz  | 1.22 | -0.9 dB |
| Peaking | 544 Hz  | 0.16 | 1.0 dB  |
| Peaking | 3636 Hz | 2.23 | 3.6 dB  |
| Peaking | 5805 Hz | 3.29 | 5.8 dB  |
| Peaking | 1027 Hz | 2.84 | -1.5 dB |
| Peaking | 1884 Hz | 1.93 | 2.9 dB  |
| Peaking | 2218 Hz | 3.77 | -3.3 dB |
| Peaking | 8281 Hz | 4.16 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurex%20HR%20V9/Aurex%20HR%20V9.png)
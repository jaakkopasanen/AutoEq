# Etymotic EK5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.7; 60 5.3; 66 4.9; 72 4.5; 79 4.1; 87 3.6; 96 3.2; 106 3.0; 116 2.8; 128 2.4; 141 2.1; 155 1.8; 170 1.7; 187 1.7; 206 1.5; 227 1.5; 249 1.5; 274 1.4; 302 1.6; 332 1.6; 365 1.7; 402 1.8; 442 1.9; 486 1.7; 535 1.8; 588 2.1; 647 2.0; 712 1.8; 783 1.8; 861 1.2; 947 0.6; 1042 -0.4; 1146 -1.3; 1261 -2.3; 1387 -2.7; 1526 -3.7; 1678 -4.9; 1846 -5.7; 2031 -6.3; 2234 -6.0; 2457 -3.1; 2703 -2.5; 2973 -0.5; 3270 1.0; 3597 2.0; 3957 2.2; 4353 1.4; 4788 1.2; 5267 1.8; 5793 2.6; 6373 3.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic EK5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic EK5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.37 | 6.3 dB  |
| Peaking | 680 Hz  | 0.69 | 2.7 dB  |
| Peaking | 2028 Hz | 1.06 | -7.9 dB |
| Peaking | 3509 Hz | 1.46 | 4.6 dB  |
| Peaking | 6343 Hz | 4.75 | 4.1 dB  |
| Peaking | 8132 Hz | 5.81 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20EK5/Etymotic%20EK5.png)
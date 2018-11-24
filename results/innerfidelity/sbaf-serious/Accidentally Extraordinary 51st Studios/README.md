# Accidentally Extraordinary 51st Studios

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.7; 28 3.7; 31 2.9; 34 2.2; 37 1.6; 41 0.9; 45 0.4; 49 -0.1; 54 -0.6; 60 -1.1; 66 -1.4; 72 -1.6; 79 -1.9; 87 -2.4; 96 -2.8; 106 -2.8; 116 -3.0; 128 -3.6; 141 -4.1; 155 -4.1; 170 -3.7; 187 -3.8; 206 -3.6; 227 -3.1; 249 -2.6; 274 -1.8; 302 -0.8; 332 0.2; 365 1.4; 402 2.0; 442 2.3; 486 2.2; 535 2.5; 588 2.8; 647 2.4; 712 1.5; 783 1.1; 861 0.4; 947 0.1; 1042 0.0; 1146 0.3; 1261 -0.6; 1387 -0.9; 1526 -0.9; 1678 -0.6; 1846 0.3; 2031 1.5; 2234 2.7; 2457 4.2; 2703 5.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 3.8; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Accidentally Extraordinary 51st Studios GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Accidentally Extraordinary 51st Studios ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.65 | 8.6 dB  |
| Peaking | 428 Hz  | 0.22 | -8.8 dB |
| Peaking | 516 Hz  | 0.61 | 11.4 dB |
| Peaking | 3071 Hz | 1.29 | 7.9 dB  |
| Peaking | 5719 Hz | 3.06 | 5.4 dB  |
| Peaking | 208 Hz  | 1.9  | -0.5 dB |
| Peaking | 367 Hz  | 5.99 | 0.8 dB  |
| Peaking | 1134 Hz | 7.39 | 1.0 dB  |
| Peaking | 1580 Hz | 4.36 | -0.7 dB |
| Peaking | 8301 Hz | 4.33 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Accidentally%20Extraordinary%2051st%20Studios/Accidentally%20Extraordinary%2051st%20Studios.png)
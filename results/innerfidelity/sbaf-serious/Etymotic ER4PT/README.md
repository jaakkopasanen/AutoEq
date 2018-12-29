# Etymotic ER4PT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.8; 60 5.4; 66 5.1; 72 4.6; 79 4.2; 87 3.8; 96 3.3; 106 3.0; 116 2.7; 128 2.3; 141 2.0; 155 1.7; 170 1.5; 187 1.5; 206 1.3; 227 1.3; 249 1.1; 274 1.1; 302 1.2; 332 1.2; 365 1.3; 402 1.3; 442 1.4; 486 1.3; 535 1.4; 588 1.7; 647 1.7; 712 1.5; 783 1.5; 861 1.1; 947 0.5; 1042 -0.3; 1146 -1.0; 1261 -1.7; 1387 -2.7; 1526 -3.6; 1678 -4.2; 1846 -4.4; 2031 -4.4; 2234 -4.3; 2457 -3.2; 2703 -2.1; 2973 0.0; 3270 1.7; 3597 2.3; 3957 1.6; 4353 -0.2; 4788 0.4; 5267 3.3; 5793 5.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.1; 9330 -0.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4PT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4PT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 34 Hz    |  0.38 | 6.3 dB  |
| Peaking | 851 Hz   |  0.67 | 5.1 dB  |
| Peaking | 2208 Hz  |  0.42 | -8.1 dB |
| Peaking | 3408 Hz  |  1.94 | 8.0 dB  |
| Peaking | 5988 Hz  |  2.96 | 8.9 dB  |
| Peaking | 6719 Hz  | 11.87 | 0.9 dB  |
| Peaking | 8615 Hz  |  6.95 | -2.4 dB |
| Peaking | 10666 Hz |  1.81 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4PT/Etymotic%20ER4PT.png)
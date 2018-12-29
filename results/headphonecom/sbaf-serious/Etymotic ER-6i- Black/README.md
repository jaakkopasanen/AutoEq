# Etymotic ER-6i- Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.7; 45 5.5; 49 5.3; 54 5.0; 60 4.6; 66 4.3; 72 4.0; 79 3.7; 87 3.1; 96 2.8; 106 2.6; 116 2.3; 128 2.0; 141 1.7; 155 1.5; 170 1.3; 187 1.2; 206 1.1; 227 0.8; 249 0.9; 274 0.9; 302 1.1; 332 1.3; 365 1.4; 402 1.1; 442 1.0; 486 1.1; 535 1.2; 588 1.4; 647 1.4; 712 1.4; 783 1.3; 861 1.0; 947 0.4; 1042 -0.4; 1146 -1.0; 1261 -1.7; 1387 -2.6; 1526 -3.7; 1678 -4.5; 1846 -5.1; 2031 -5.5; 2234 -5.3; 2457 -4.5; 2703 -3.0; 2973 -0.9; 3270 1.4; 3597 2.9; 3957 2.2; 4353 0.5; 4788 0.4; 5267 2.7; 5793 5.1; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.1; 9330 -0.9; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-6i- Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i- Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.17 | 6.2 dB  |
| Peaking | 2062 Hz | 1.71 | -6.2 dB |
| Peaking | 3550 Hz | 4.41 | 4.1 dB  |
| Peaking | 6148 Hz | 3.65 | 6.4 dB  |
| Peaking | 8675 Hz | 5.53 | -3.0 dB |
| Peaking | 360 Hz  | 4.05 | 0.8 dB  |
| Peaking | 710 Hz  | 1.4  | 1.7 dB  |
| Peaking | 1254 Hz | 3.25 | -0.7 dB |
| Peaking | 1540 Hz | 5.83 | -0.9 dB |
| Peaking | 9892 Hz | 5.99 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i-%20Black/Etymotic%20ER-6i-%20Black.png)
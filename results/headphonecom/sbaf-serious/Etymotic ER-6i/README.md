# Etymotic ER-6i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.6; 28 5.4; 31 5.3; 34 5.3; 37 5.1; 41 4.9; 45 4.7; 49 4.6; 54 4.4; 60 4.1; 66 3.6; 72 3.3; 79 3.0; 87 2.7; 96 2.4; 106 2.1; 116 1.9; 128 1.6; 141 1.3; 155 1.0; 170 0.9; 187 0.7; 206 0.7; 227 0.6; 249 0.6; 274 0.6; 302 0.7; 332 0.8; 365 0.8; 402 0.8; 442 0.7; 486 0.8; 535 1.0; 588 1.2; 647 1.2; 712 1.3; 783 1.2; 861 0.9; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -2.2; 1526 -3.0; 1678 -3.7; 1846 -4.4; 2031 -4.4; 2234 -4.1; 2457 -3.2; 2703 -2.1; 2973 -0.3; 3270 1.7; 3597 2.8; 3957 2.0; 4353 0.4; 4788 0.7; 5267 3.5; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-6i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.36 | 3.6 dB  |
| Peaking | 2008 Hz | 1.8  | -5.0 dB |
| Peaking | 3534 Hz | 4.65 | 3.6 dB  |
| Peaking | 6002 Hz | 3.98 | 6.7 dB  |
| Peaking | 19 Hz   | 0.94 | 2.7 dB  |
| Peaking | 48 Hz   | 1.79 | 0.7 dB  |
| Peaking | 714 Hz  | 1.16 | 1.6 dB  |
| Peaking | 1350 Hz | 2.27 | -1.0 dB |
| Peaking | 8201 Hz | 5.46 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i/Etymotic%20ER-6i.png)
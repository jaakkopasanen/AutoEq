# Etymotic MC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 5.1; 72 4.8; 79 4.3; 87 4.0; 96 3.5; 106 3.2; 116 3.0; 128 2.7; 141 2.4; 155 2.2; 170 2.0; 187 1.8; 206 1.8; 227 1.5; 249 1.5; 274 1.5; 302 1.6; 332 1.7; 365 1.9; 402 2.0; 442 1.9; 486 2.0; 535 1.9; 588 2.1; 647 2.1; 712 2.0; 783 1.7; 861 1.2; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -2.0; 1387 -3.0; 1526 -4.0; 1678 -3.9; 1846 -3.8; 2031 -3.2; 2234 -2.3; 2457 -1.1; 2703 0.4; 2973 2.0; 3270 3.9; 3597 5.6; 3957 5.5; 4353 4.2; 4788 3.9; 5267 5.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic MC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.35 | 6.3 dB  |
| Peaking | 755 Hz  | 0.62 | 3.1 dB  |
| Peaking | 1661 Hz | 1    | -6.0 dB |
| Peaking | 3661 Hz | 2.06 | 6.5 dB  |
| Peaking | 5883 Hz | 3.45 | 5.8 dB  |
| Peaking | 8099 Hz | 4.8  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC3/Etymotic%20MC3.png)
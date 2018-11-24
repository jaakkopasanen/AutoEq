# Etymotic MC5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.7; 60 5.2; 66 4.9; 72 4.6; 79 4.3; 87 3.9; 96 3.5; 106 3.2; 116 3.0; 128 2.7; 141 2.4; 155 2.2; 170 2.0; 187 1.8; 206 1.8; 227 1.7; 249 1.7; 274 1.7; 302 1.8; 332 2.0; 365 2.1; 402 2.2; 442 2.1; 486 2.2; 535 2.2; 588 2.2; 647 2.2; 712 2.1; 783 1.9; 861 1.4; 947 0.6; 1042 -0.3; 1146 -1.2; 1261 -2.3; 1387 -3.5; 1526 -4.8; 1678 -5.6; 1846 -4.9; 2031 -2.1; 2234 -1.3; 2457 -0.3; 2703 1.2; 2973 2.9; 3270 4.7; 3597 6.0; 3957 6.0; 4353 5.2; 4788 5.1; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic MC5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.34 | 6.2 dB  |
| Peaking | 617 Hz  | 0.66 | 2.5 dB  |
| Peaking | 1641 Hz | 1.71 | -6.8 dB |
| Peaking | 3705 Hz | 1.89 | 6.2 dB  |
| Peaking | 5780 Hz | 3.16 | 5.3 dB  |
| Peaking | 1064 Hz | 1.35 | 0.3 dB  |
| Peaking | 1115 Hz | 3.78 | -0.6 dB |
| Peaking | 6628 Hz | 8.23 | 2.0 dB  |
| Peaking | 7841 Hz | 2.39 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC5/Etymotic%20MC5.png)
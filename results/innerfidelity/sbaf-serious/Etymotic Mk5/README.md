# Etymotic Mk5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 5.6; 66 5.2; 72 4.9; 79 4.5; 87 4.0; 96 3.4; 106 3.1; 116 2.9; 128 2.6; 141 2.4; 155 2.2; 170 2.0; 187 1.8; 206 1.8; 227 1.7; 249 1.6; 274 1.7; 302 1.8; 332 1.8; 365 1.9; 402 1.8; 442 2.0; 486 1.9; 535 2.0; 588 2.2; 647 2.2; 712 1.9; 783 1.8; 861 1.2; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -2.1; 1387 -3.3; 1526 -4.5; 1678 -5.5; 1846 -6.0; 2031 -6.3; 2234 -6.2; 2457 -5.1; 2703 -3.5; 2973 -1.5; 3270 -0.3; 3597 -0.7; 3957 -0.7; 4353 0.7; 4788 2.7; 5267 3.5; 5793 2.9; 6373 3.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Mk5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Mk5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.36 | 6.3 dB  |
| Peaking | 660 Hz  | 0.64 | 2.5 dB  |
| Peaking | 1659 Hz | 1.36 | -5.3 dB |
| Peaking | 2250 Hz | 2.55 | -4.0 dB |
| Peaking | 5606 Hz | 2.17 | 4.0 dB  |
| Peaking | 3267 Hz | 7.23 | 1.0 dB  |
| Peaking | 3926 Hz | 7.42 | -1.1 dB |
| Peaking | 6768 Hz | 8.83 | 2.3 dB  |
| Peaking | 7648 Hz | 2.28 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20Mk5/Etymotic%20Mk5.png)
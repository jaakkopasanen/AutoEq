# Etymotic hf5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.4; 116 4.5; 128 3.6; 141 2.9; 155 2.2; 170 1.8; 187 1.2; 206 0.7; 227 0.4; 249 0.4; 274 0.4; 302 0.5; 332 0.6; 365 0.6; 402 0.7; 442 0.8; 486 0.9; 535 1.1; 588 1.2; 647 1.5; 712 1.5; 783 1.3; 861 0.9; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.7; 1387 -2.5; 1526 -3.3; 1678 -3.7; 1846 -3.8; 2031 -3.6; 2234 -2.9; 2457 -1.8; 2703 -0.9; 2973 -0.1; 3270 0.9; 3597 1.0; 3957 -0.5; 4353 -1.7; 4788 -0.5; 5267 2.9; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.4  | 6.8 dB  |
| Peaking | 719 Hz  | 2.08 | 1.8 dB  |
| Peaking | 1756 Hz | 1.78 | -4.3 dB |
| Peaking | 4519 Hz | 6.91 | -2.9 dB |
| Peaking | 5972 Hz | 3.6  | 6.7 dB  |
| Peaking | 16 Hz   | 1.13 | 2.1 dB  |
| Peaking | 42 Hz   | 1.09 | -1.2 dB |
| Peaking | 99 Hz   | 2.56 | 1.7 dB  |
| Peaking | 212 Hz  | 1.88 | -1.2 dB |
| Peaking | 3370 Hz | 6.45 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Etymotic%20hf5/Etymotic%20hf5.png)
# Etymotic hf5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.7; 54 5.5; 60 5.2; 66 4.8; 72 4.5; 79 4.1; 87 3.6; 96 3.3; 106 2.4; 116 2.4; 128 1.9; 141 1.4; 155 1.1; 170 0.9; 187 0.7; 206 0.6; 227 0.4; 249 0.4; 274 0.3; 302 0.3; 332 0.3; 365 0.3; 402 0.3; 442 0.2; 486 0.2; 535 0.2; 588 0.3; 647 0.4; 712 0.5; 783 0.6; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.4; 1387 -1.7; 1526 -1.6; 1678 -1.3; 1846 -0.8; 2031 -0.5; 2234 -0.3; 2457 -0.3; 2703 -0.2; 2973 0.0; 3270 0.4; 3597 0.9; 3957 1.6; 4353 2.5; 4788 3.8; 5267 5.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.4; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.44 | 6.4 dB  |
| Peaking | 866 Hz  | 1.95 | 1.2 dB  |
| Peaking | 1386 Hz | 1.5  | -2.0 dB |
| Peaking | 5641 Hz | 2.59 | 6.6 dB  |
| Peaking | 35 Hz   | 1.99 | -0.4 dB |
| Peaking | 72 Hz   | 2.7  | 0.4 dB  |
| Peaking | 6608 Hz | 7.63 | 2.1 dB  |
| Peaking | 7786 Hz | 2.43 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20hf5/Etymotic%20hf5.png)
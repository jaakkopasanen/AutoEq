# Turtle Beach Stealth 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.2; 28 -0.4; 31 -0.8; 34 -1.0; 37 -1.2; 41 -1.3; 45 -1.4; 49 -1.5; 54 -1.5; 60 -1.5; 66 -1.6; 72 -1.7; 79 -1.6; 87 -1.6; 96 -1.6; 106 -1.6; 116 -1.6; 128 -1.6; 141 -1.5; 155 -1.3; 170 -1.0; 187 -0.8; 206 -0.4; 227 0.0; 249 0.4; 274 0.7; 302 0.9; 332 1.2; 365 1.6; 402 2.1; 442 2.4; 486 2.3; 535 2.1; 588 1.9; 647 1.9; 712 1.9; 783 1.6; 861 1.1; 947 0.3; 1042 -0.1; 1146 -0.2; 1261 0.0; 1387 0.3; 1526 1.1; 1678 2.1; 1846 2.8; 2031 3.1; 2234 4.0; 2457 4.3; 2703 4.6; 2973 6.0; 3270 5.7; 3597 4.7; 3957 1.2; 4353 1.3; 4788 3.2; 5267 5.9; 5793 6.0; 6373 2.0; 7010 1.6; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.63 | 1.9 dB  |
| Peaking | 75 Hz   | 0.37 | -1.9 dB |
| Peaking | 451 Hz  | 1.08 | 2.7 dB  |
| Peaking | 2851 Hz | 1.69 | 5.7 dB  |
| Peaking | 5574 Hz | 4.94 | 6.0 dB  |
| Peaking | 16 Hz   | 1.04 | 1.2 dB  |
| Peaking | 1175 Hz | 3.37 | -1.2 dB |
| Peaking | 1828 Hz | 4.67 | 1.1 dB  |
| Peaking | 3480 Hz | 7.79 | 1.8 dB  |
| Peaking | 4055 Hz | 7.17 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Turtle%20Beach%20Stealth%20600/Turtle%20Beach%20Stealth%20600.png)
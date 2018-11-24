# Blue MOFI Active On Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.5; 28 0.0; 31 -0.4; 34 -0.9; 37 -1.3; 41 -1.9; 45 -2.5; 49 -3.0; 54 -3.6; 60 -4.2; 66 -4.6; 72 -4.8; 79 -4.8; 87 -4.6; 96 -4.5; 106 -4.2; 116 -3.7; 128 -3.4; 141 -3.6; 155 -3.6; 170 -2.6; 187 -3.0; 206 -2.8; 227 -2.1; 249 -1.3; 274 -0.1; 302 0.8; 332 1.1; 365 1.1; 402 1.1; 442 2.7; 486 3.3; 535 2.8; 588 2.6; 647 2.3; 712 1.7; 783 1.4; 861 0.8; 947 0.1; 1042 -0.0; 1146 0.1; 1261 0.1; 1387 -0.1; 1526 -0.4; 1678 -0.3; 1846 0.2; 2031 1.3; 2234 2.2; 2457 2.4; 2703 3.4; 2973 3.9; 3270 4.2; 3597 5.1; 3957 3.4; 4353 -0.0; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Active On Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 76 Hz   | 1.01 | -4.8 dB |
| Peaking | 173 Hz  | 1.38 | -2.4 dB |
| Peaking | 500 Hz  | 1.55 | 3.4 dB  |
| Peaking | 3173 Hz | 2.26 | 4.3 dB  |
| Peaking | 5718 Hz | 3.16 | 6.4 dB  |
| Peaking | 19 Hz   | 1.94 | 1.6 dB  |
| Peaking | 703 Hz  | 4.49 | 0.5 dB  |
| Peaking | 1800 Hz | 1.45 | -1.6 dB |
| Peaking | 2181 Hz | 2.84 | 2.0 dB  |
| Peaking | 8286 Hz | 4.85 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On%20Plus/Blue%20MOFI%20Active%20On%20Plus.png)
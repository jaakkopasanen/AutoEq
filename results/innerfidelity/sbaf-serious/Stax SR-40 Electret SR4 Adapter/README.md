# Stax SR-40 Electret SR4 Adapter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.3; 106 3.6; 116 2.0; 128 0.4; 141 -0.6; 155 -1.2; 170 -1.3; 187 -1.3; 206 -1.0; 227 -0.8; 249 -0.6; 274 -0.3; 302 -0.1; 332 0.1; 365 0.3; 402 0.4; 442 0.5; 486 0.4; 535 0.1; 588 0.3; 647 0.6; 712 0.5; 783 0.5; 861 0.0; 947 0.1; 1042 0.2; 1146 0.0; 1261 -1.1; 1387 -2.5; 1526 -4.0; 1678 -4.7; 1846 -3.4; 2031 -0.4; 2234 0.7; 2457 2.7; 2703 4.1; 2973 4.1; 3270 4.0; 3597 2.6; 3957 2.0; 4353 1.8; 4788 1.2; 5267 1.5; 5793 1.8; 6373 1.3; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-40 Electret SR4 Adapter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-40 Electret SR4 Adapter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 60 Hz   | 0.28 | 7.4 dB  |
| Peaking | 166 Hz  | 1.07 | -6.5 dB |
| Peaking | 1679 Hz | 2.83 | -6.2 dB |
| Peaking | 2891 Hz | 1.56 | 4.7 dB  |
| Peaking | 6615 Hz | 3.85 | 1.6 dB  |
| Peaking | 19 Hz   | 1.26 | 1.7 dB  |
| Peaking | 45 Hz   | 1.08 | -0.9 dB |
| Peaking | 90 Hz   | 3.49 | 1.6 dB  |
| Peaking | 127 Hz  | 4.47 | -0.9 dB |
| Peaking | 1095 Hz | 7.72 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-40%20Electret%20SR4%20Adapter/Stax%20SR-40%20Electret%20SR4%20Adapter.png)
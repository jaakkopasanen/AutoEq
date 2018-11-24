# Sennheiser Momentum M2 OEBT Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.6; 23 -2.0; 25 -2.3; 28 -2.8; 31 -3.1; 34 -3.4; 37 -3.6; 41 -4.0; 45 -4.3; 49 -4.6; 54 -4.9; 60 -5.2; 66 -5.1; 72 -4.9; 79 -5.9; 87 -6.5; 96 -6.1; 106 -5.6; 116 -6.7; 128 -7.7; 141 -8.0; 155 -7.6; 170 -6.9; 187 -6.6; 206 -5.2; 227 -3.3; 249 -1.5; 274 0.1; 302 1.1; 332 1.2; 365 0.8; 402 0.1; 442 0.3; 486 0.3; 535 0.5; 588 0.7; 647 0.6; 712 0.5; 783 0.6; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 -1.2; 1526 -2.1; 1678 -2.9; 1846 -3.3; 2031 -3.5; 2234 -3.4; 2457 -2.7; 2703 -1.7; 2973 -0.2; 3270 1.7; 3597 3.4; 3957 5.9; 4353 5.7; 4788 2.0; 5267 0.8; 5793 3.1; 6373 2.0; 7010 -0.8; 7711 -1.6; 8482 -3.6; 9330 -5.4; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 OEBT Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.13 | -4.3 dB |
| Peaking | 67 Hz   | 0.75 | -5.1 dB |
| Peaking | 151 Hz  | 1.86 | -6.6 dB |
| Peaking | 4132 Hz | 4.46 | 6.9 dB  |
| Peaking | 9080 Hz | 5    | -5.9 dB |
| Peaking | 203 Hz  | 4.81 | -2.1 dB |
| Peaking | 307 Hz  | 2.96 | 2.4 dB  |
| Peaking | 817 Hz  | 0.67 | 1.0 dB  |
| Peaking | 2141 Hz | 1.19 | -6.1 dB |
| Peaking | 3030 Hz | 0.79 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive.png)
# Sennheiser Momentum Wireless Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.5; 28 1.1; 31 0.7; 34 0.5; 37 0.2; 41 -0.0; 45 -0.2; 49 -0.4; 54 -0.5; 60 -0.8; 66 -1.0; 72 -1.2; 79 -1.5; 87 -1.8; 96 -2.2; 106 -2.3; 116 -2.3; 128 -2.2; 141 -1.9; 155 -2.2; 170 -1.7; 187 -1.2; 206 -0.9; 227 -0.3; 249 0.3; 274 0.7; 302 1.5; 332 2.1; 365 2.1; 402 1.5; 442 1.2; 486 0.8; 535 0.5; 588 0.5; 647 0.5; 712 0.3; 783 0.5; 861 0.3; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.2; 1526 -1.8; 1678 -1.8; 1846 -2.1; 2031 -1.6; 2234 -0.6; 2457 1.0; 2703 2.4; 2973 4.4; 3270 5.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 2.7; 5267 3.5; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum Wireless Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.97 | 3.2 dB  |
| Peaking | 121 Hz  | 0.72 | -2.5 dB |
| Peaking | 341 Hz  | 1.88 | 2.8 dB  |
| Peaking | 3715 Hz | 2.5  | 6.8 dB  |
| Peaking | 6024 Hz | 4.36 | 5.6 dB  |
| Peaking | 1811 Hz | 2.11 | -2.8 dB |
| Peaking | 2964 Hz | 4.73 | 2.0 dB  |
| Peaking | 6704 Hz | 8.5  | 1.7 dB  |
| Peaking | 7744 Hz | 2.46 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Wired%20Passive/Sennheiser%20Momentum%20Wireless%20Wired%20Passive.png)
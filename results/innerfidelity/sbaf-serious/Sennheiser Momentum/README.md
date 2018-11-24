# Sennheiser Momentum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 3.2; 28 2.9; 31 2.8; 34 2.6; 37 2.5; 41 2.3; 45 2.1; 49 2.0; 54 1.7; 60 1.5; 66 1.3; 72 1.0; 79 0.7; 87 0.3; 96 -0.1; 106 -0.3; 116 -0.3; 128 -0.3; 141 -0.3; 155 -1.1; 170 -0.8; 187 -1.0; 206 -1.3; 227 -1.2; 249 -1.1; 274 -0.7; 302 -0.3; 332 0.1; 365 0.7; 402 1.2; 442 1.5; 486 1.4; 535 1.5; 588 1.5; 647 1.2; 712 0.7; 783 0.6; 861 0.2; 947 -0.0; 1042 0.0; 1146 0.1; 1261 -0.0; 1387 -0.8; 1526 -1.4; 1678 -1.4; 1846 -0.8; 2031 0.2; 2234 1.6; 2457 3.7; 2703 5.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.31 | 3.4 dB  |
| Peaking | 49 Hz   | 2.08 | 1.6 dB  |
| Peaking | 527 Hz  | 2.52 | 1.7 dB  |
| Peaking | 1704 Hz | 2.06 | -3.6 dB |
| Peaking | 3811 Hz | 0.88 | 7.1 dB  |
| Peaking | 204 Hz  | 1.83 | -1.5 dB |
| Peaking | 2826 Hz | 4.91 | 1.3 dB  |
| Peaking | 3839 Hz | 2.8  | -1.0 dB |
| Peaking | 6280 Hz | 2.45 | 5.3 dB  |
| Peaking | 7355 Hz | 1.5  | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)
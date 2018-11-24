# Monster Turbine Pro Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -9.0; 23 -9.0; 25 -9.0; 28 -9.0; 31 -8.9; 34 -8.9; 37 -8.9; 41 -8.9; 45 -8.9; 49 -8.8; 54 -8.8; 60 -8.8; 66 -8.9; 72 -8.9; 79 -8.9; 87 -9.0; 96 -9.0; 106 -8.8; 116 -8.6; 128 -8.4; 141 -8.2; 155 -7.8; 170 -7.5; 187 -7.1; 206 -6.5; 227 -6.0; 249 -5.4; 274 -4.9; 302 -4.3; 332 -3.7; 365 -3.1; 402 -2.5; 442 -1.8; 486 -1.4; 535 -0.8; 588 -0.1; 647 0.3; 712 0.5; 783 0.8; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.7; 1526 -2.7; 1678 -3.5; 1846 -4.0; 2031 -4.2; 2234 -4.4; 2457 -3.9; 2703 -3.0; 2973 -0.6; 3270 1.6; 3597 2.2; 3957 0.9; 4353 -2.1; 4788 -2.8; 5267 -0.9; 5793 2.1; 6373 4.4; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.5; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine Pro Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine Pro Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.22 | -9.6 dB |
| Peaking | 2182 Hz | 1.89 | -5.0 dB |
| Peaking | 3581 Hz | 3.3  | 4.5 dB  |
| Peaking | 4637 Hz | 3.23 | -4.0 dB |
| Peaking | 6361 Hz | 4.9  | 5.5 dB  |
| Peaking | 16 Hz   | 2.8  | -1.2 dB |
| Peaking | 200 Hz  | 1.32 | -1.0 dB |
| Peaking | 727 Hz  | 1.35 | 2.1 dB  |
| Peaking | 1577 Hz | 3.93 | -1.3 dB |
| Peaking | 9391 Hz | 7.3  | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine%20Pro%20Gold/Monster%20Turbine%20Pro%20Gold.png)
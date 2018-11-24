# HiFiMAN RE-600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.1; 25 4.0; 28 3.9; 31 3.8; 34 3.7; 37 3.6; 41 3.5; 45 3.4; 49 3.2; 54 2.9; 60 2.6; 66 2.3; 72 2.0; 79 1.6; 87 1.2; 96 0.8; 106 0.5; 116 0.4; 128 0.1; 141 -0.2; 155 -0.3; 170 -0.4; 187 -0.5; 206 -0.5; 227 -0.4; 249 -0.3; 274 -0.2; 302 0.0; 332 0.2; 365 0.4; 402 0.6; 442 1.0; 486 1.0; 535 1.2; 588 1.5; 647 1.6; 712 1.5; 783 1.5; 861 1.0; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -2.0; 1387 -3.3; 1526 -4.7; 1678 -5.9; 1846 -5.5; 2031 -4.7; 2234 -3.0; 2457 0.8; 2703 4.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.6; 5793 5.1; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.96 | 4.0 dB   |
| Peaking | 53 Hz   | 1.53 | 2.1 dB   |
| Peaking | 726 Hz  | 1.37 | 2.2 dB   |
| Peaking | 1865 Hz | 1.39 | -10.8 dB |
| Peaking | 3361 Hz | 0.84 | 9.5 dB   |
| Peaking | 189 Hz  | 1.95 | -0.8 dB  |
| Peaking | 2821 Hz | 7.79 | 1.9 dB   |
| Peaking | 3634 Hz | 3.87 | -1.1 dB  |
| Peaking | 6390 Hz | 2.41 | 5.2 dB   |
| Peaking | 7430 Hz | 1.59 | -4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-600/HiFiMAN%20RE-600.png)
# BKHC BK9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.4; 25 3.0; 28 2.5; 31 2.2; 34 1.9; 37 1.6; 41 1.4; 45 1.2; 49 1.0; 54 0.9; 60 0.7; 66 0.5; 72 0.4; 79 0.2; 87 0.2; 96 0.2; 106 -0.4; 116 -0.3; 128 0.5; 141 0.2; 155 0.0; 170 0.0; 187 -0.1; 206 -0.4; 227 -1.0; 249 -1.2; 274 -1.4; 302 -1.4; 332 -1.6; 365 -2.0; 402 -2.3; 442 -2.5; 486 -2.9; 535 -3.2; 588 -3.0; 647 -3.1; 712 -2.9; 783 -1.9; 861 -0.6; 947 -0.2; 1042 0.6; 1146 2.0; 1261 3.5; 1387 4.6; 1526 5.6; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BKHC BK9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BKHC BK9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.82 | 4.2 dB  |
| Peaking | 40 Hz   | 0.1  | 0.2 dB  |
| Peaking | 670 Hz  | 0.72 | -5.4 dB |
| Peaking | 1864 Hz | 0.61 | 7.4 dB  |
| Peaking | 5108 Hz | 1.84 | 4.5 dB  |
| Peaking | 2260 Hz | 2.68 | -1.0 dB |
| Peaking | 3956 Hz | 0.81 | 1.3 dB  |
| Peaking | 4868 Hz | 3.91 | -1.2 dB |
| Peaking | 6392 Hz | 4.04 | 3.7 dB  |
| Peaking | 7301 Hz | 1.41 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BKHC%20BK9/BKHC%20BK9.png)
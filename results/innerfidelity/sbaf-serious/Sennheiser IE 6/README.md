# Sennheiser IE 6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.1; 28 -4.4; 31 -4.8; 34 -5.1; 37 -5.3; 41 -5.7; 45 -6.0; 49 -6.2; 54 -6.5; 60 -6.9; 66 -7.2; 72 -7.5; 79 -7.8; 87 -8.2; 96 -8.4; 106 -8.6; 116 -8.6; 128 -8.7; 141 -8.7; 155 -8.7; 170 -8.5; 187 -8.3; 206 -8.0; 227 -7.6; 249 -7.2; 274 -6.7; 302 -6.2; 332 -5.6; 365 -4.9; 402 -4.3; 442 -3.6; 486 -3.1; 535 -2.4; 588 -1.5; 647 -0.9; 712 -0.5; 783 0.1; 861 0.2; 947 0.1; 1042 -0.0; 1146 0.0; 1261 -0.2; 1387 -0.6; 1526 -0.7; 1678 -1.1; 1846 -1.2; 2031 -1.1; 2234 -1.2; 2457 -1.1; 2703 -1.4; 2973 -0.6; 3270 0.0; 3597 -0.1; 3957 -2.4; 4353 -7.4; 4788 -9.4; 5267 -2.8; 5793 2.8; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 58 Hz   | 0.37 | -5.5 dB  |
| Peaking | 152 Hz  | 0.74 | -4.9 dB  |
| Peaking | 302 Hz  | 1.23 | -2.9 dB  |
| Peaking | 4700 Hz | 4.83 | -11.2 dB |
| Peaking | 6271 Hz | 4.46 | 7.0 dB   |
| Peaking | 488 Hz  | 2.53 | -0.8 dB  |
| Peaking | 854 Hz  | 1.23 | 1.2 dB   |
| Peaking | 2083 Hz | 1.07 | -1.2 dB  |
| Peaking | 3456 Hz | 5.82 | 2.0 dB   |
| Peaking | 7897 Hz | 7.42 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%206/Sennheiser%20IE%206.png)
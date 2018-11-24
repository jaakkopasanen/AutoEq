# Plantronics BackBeat Pro 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 -8.6; 23 -8.8; 25 -8.9; 28 -8.9; 31 -9.1; 34 -9.3; 37 -9.3; 41 -8.7; 45 -7.7; 49 -6.5; 54 -5.1; 60 -3.6; 66 -2.3; 72 -1.3; 79 -0.3; 87 0.5; 96 1.2; 106 1.8; 116 2.2; 128 2.5; 141 2.9; 155 3.1; 170 3.2; 187 3.2; 206 3.0; 227 2.8; 249 2.5; 274 2.2; 302 2.0; 332 1.9; 365 1.7; 402 0.9; 442 0.1; 486 -0.4; 535 -0.5; 588 -0.3; 647 0.8; 712 0.8; 783 -0.1; 861 -0.1; 947 0.0; 1042 -0.0; 1146 0.0; 1261 -0.1; 1387 -0.7; 1526 -0.4; 1678 -1.2; 1846 -1.9; 2031 -1.4; 2234 -0.3; 2457 0.2; 2703 0.4; 2973 0.3; 3270 0.2; 3597 -0.3; 3957 -0.7; 4353 -1.4; 4788 0.2; 5267 2.1; 5793 2.5; 6373 1.8; 7010 0.3; 7711 -1.2; 8482 -1.8; 9330 -2.0; 10263 -1.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Pro 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Pro 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.57 | -10.7 dB |
| Peaking | 121 Hz  | 0.56 | 5.1 dB   |
| Peaking | 1835 Hz | 4.18 | -2.1 dB  |
| Peaking | 5879 Hz | 4.41 | 3.1 dB   |
| Peaking | 8796 Hz | 2.85 | -2.4 dB  |
| Peaking | 125 Hz  | 3.29 | -0.5 dB  |
| Peaking | 357 Hz  | 0.96 | 0.6 dB   |
| Peaking | 491 Hz  | 2.93 | -1.8 dB  |
| Peaking | 4412 Hz | 4.97 | -3.1 dB  |
| Peaking | 4780 Hz | 2.97 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Plantronics%20BackBeat%20Pro%202/Plantronics%20BackBeat%20Pro%202.png)
# Plantronics BackBeat Pro 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -9.0; 23 -9.1; 25 -9.1; 28 -9.1; 31 -9.1; 34 -9.3; 37 -9.2; 41 -8.5; 45 -7.4; 49 -6.2; 54 -4.7; 60 -3.3; 66 -2.2; 72 -1.3; 79 -0.5; 87 0.2; 96 0.8; 106 1.3; 116 1.7; 128 2.0; 141 2.3; 155 2.5; 170 2.6; 187 2.6; 206 2.5; 227 2.3; 249 2.0; 274 1.5; 302 1.2; 332 1.0; 365 0.6; 402 -0.1; 442 -1.1; 486 -1.6; 535 -1.7; 588 -1.4; 647 -0.2; 712 -0.1; 783 -0.5; 861 -0.3; 947 0.0; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 -0.0; 1678 -0.8; 1846 -1.9; 2031 -1.8; 2234 -0.8; 2457 -0.2; 2703 -0.2; 2973 -0.7; 3270 -1.6; 3597 -2.4; 3957 -1.8; 4353 -1.4; 4788 0.3; 5267 1.7; 5793 1.0; 6373 -0.8; 7010 -2.2; 7711 -2.3; 8482 -2.2; 9330 -3.5; 10263 -4.5; 11289 -2.5; 12418 -0.1; 13660 -0.4; 15026 -1.5; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Pro 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Pro 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.49 | -12.5 dB |
| Peaking | 94 Hz   | 0.4  | 5.9 dB   |
| Peaking | 497 Hz  | 2.28 | -2.7 dB  |
| Peaking | 2464 Hz | 0.82 | -1.2 dB  |
| Peaking | 9885 Hz | 2.56 | -4.4 dB  |
| Peaking | 1969 Hz | 4.05 | -2.2 dB  |
| Peaking | 2758 Hz | 1.18 | 2.5 dB   |
| Peaking | 3629 Hz | 1.82 | -3.4 dB  |
| Peaking | 5300 Hz | 3.27 | 3.1 dB   |
| Peaking | 7024 Hz | 4.9  | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Plantronics%20BackBeat%20Pro%202/Plantronics%20BackBeat%20Pro%202.png)
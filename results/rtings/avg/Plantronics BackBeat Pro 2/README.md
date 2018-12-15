# Plantronics BackBeat Pro 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -9.0; 23 -9.1; 25 -9.1; 28 -9.1; 31 -9.1; 34 -9.3; 37 -9.2; 41 -8.5; 45 -7.4; 49 -6.2; 54 -4.7; 60 -3.3; 66 -2.2; 72 -1.3; 79 -0.5; 87 0.2; 96 0.8; 106 1.3; 116 1.7; 128 2.0; 141 2.3; 155 2.5; 170 2.6; 187 2.6; 206 2.5; 227 2.3; 249 2.0; 274 1.5; 302 1.2; 332 1.0; 365 0.6; 402 -0.1; 442 -1.1; 486 -1.6; 535 -1.7; 588 -1.4; 647 -0.2; 712 -0.1; 783 -0.5; 861 -0.3; 947 0.0; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 -0.0; 1678 -0.8; 1846 -1.9; 2031 -1.8; 2234 -0.8; 2457 -0.3; 2703 -0.5; 2973 -1.2; 3270 -2.4; 3597 -3.4; 3957 -3.1; 4353 -2.7; 4788 -1.4; 5267 -0.9; 5793 -1.4; 6373 -2.0; 7010 -3.1; 7711 -3.7; 8482 -2.9; 9330 -2.2; 10263 -2.7; 11289 -3.3; 12418 -3.2; 13660 -3.7; 15026 -4.1; 16529 -0.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Pro 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Pro 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.68 | -10.3 dB |
| Peaking | 132 Hz   | 0.8  | 3.8 dB   |
| Peaking | 3679 Hz  | 3.07 | -2.8 dB  |
| Peaking | 11267 Hz | 0.58 | -3.4 dB  |
| Peaking | 24000 Hz | 1.89 | -2.4 dB  |
| Peaking | 516 Hz   | 3.42 | -2.3 dB  |
| Peaking | 1899 Hz  | 5.71 | -1.9 dB  |
| Peaking | 7541 Hz  | 4.7  | -2.1 dB  |
| Peaking | 14468 Hz | 2.03 | -3.5 dB  |
| Peaking | 15444 Hz | 0.42 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Pro%202/Plantronics%20BackBeat%20Pro%202.png)
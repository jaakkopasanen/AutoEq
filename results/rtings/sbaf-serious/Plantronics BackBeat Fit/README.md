# Plantronics BackBeat Fit

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 0.0; 23 1.6; 25 0.7; 28 -0.5; 31 -1.5; 34 -2.5; 37 -3.4; 41 -4.4; 45 -5.3; 49 -6.1; 54 -6.9; 60 -7.8; 66 -8.3; 72 -8.6; 79 -8.9; 87 -9.2; 96 -9.4; 106 -9.6; 116 -9.7; 128 -9.7; 141 -9.7; 155 -9.6; 170 -9.5; 187 -9.4; 206 -9.3; 227 -9.1; 249 -8.8; 274 -8.5; 302 -8.1; 332 -7.7; 365 -7.3; 402 -7.0; 442 -6.5; 486 -6.0; 535 -5.8; 588 -5.3; 647 -4.6; 712 -3.6; 783 -2.6; 861 -1.3; 947 -0.3; 1042 0.2; 1146 0.7; 1261 1.2; 1387 1.7; 1526 2.3; 1678 2.6; 1846 2.4; 2031 1.8; 2234 1.3; 2457 0.6; 2703 -0.4; 2973 -0.2; 3270 0.9; 3597 1.2; 3957 -0.6; 4353 -2.8; 4788 -3.7; 5267 -0.2; 5793 2.7; 6373 2.1; 7010 0.6; 7711 -0.6; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.74 | 5.8 dB  |
| Peaking | 65 Hz   | 0.44 | -5.0 dB |
| Peaking | 263 Hz  | 0.25 | -7.7 dB |
| Peaking | 1350 Hz | 0.78 | 5.0 dB  |
| Peaking | 4591 Hz | 7.7  | -4.7 dB |
| Peaking | 920 Hz  | 5.07 | 0.9 dB  |
| Peaking | 1822 Hz | 2.37 | 2.6 dB  |
| Peaking | 1912 Hz | 1.28 | -1.9 dB |
| Peaking | 5004 Hz | 9.23 | -1.7 dB |
| Peaking | 5899 Hz | 4.93 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Plantronics%20BackBeat%20Fit/Plantronics%20BackBeat%20Fit.png)
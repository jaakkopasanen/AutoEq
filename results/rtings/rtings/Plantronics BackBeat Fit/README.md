# Plantronics BackBeat Fit

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 0.5; 28 -0.6; 31 -1.6; 34 -2.5; 37 -3.3; 41 -4.2; 45 -5.0; 49 -5.8; 54 -6.6; 60 -7.5; 66 -8.1; 72 -8.6; 79 -9.1; 87 -9.6; 96 -9.9; 106 -10.1; 116 -10.2; 128 -10.2; 141 -10.2; 155 -10.2; 170 -10.1; 187 -10.0; 206 -9.8; 227 -9.6; 249 -9.4; 274 -9.2; 302 -8.9; 332 -8.6; 365 -8.3; 402 -8.0; 442 -7.6; 486 -7.2; 535 -6.9; 588 -6.4; 647 -5.6; 712 -4.5; 783 -3.1; 861 -1.5; 947 -0.4; 1042 0.2; 1146 0.5; 1261 1.0; 1387 1.8; 1526 2.6; 1678 3.0; 1846 2.4; 2031 1.3; 2234 0.8; 2457 0.2; 2703 -1.0; 2973 -1.3; 3270 -1.0; 3597 -1.0; 3957 -1.8; 4353 -2.8; 4788 -3.5; 5267 -0.7; 5793 1.3; 6373 -0.4; 7010 -1.9; 7711 -1.7; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.88 | 4.9 dB  |
| Peaking | 83 Hz   | 0.47 | -6.5 dB |
| Peaking | 601 Hz  | 0.2  | -9.2 dB |
| Peaking | 1379 Hz | 0.7  | 10.4 dB |
| Peaking | 4560 Hz | 6.6  | -3.0 dB |
| Peaking | 935 Hz  | 2.91 | 2.2 dB  |
| Peaking | 1421 Hz | 0.93 | -2.8 dB |
| Peaking | 1703 Hz | 1.99 | 3.2 dB  |
| Peaking | 5797 Hz | 7.27 | 2.8 dB  |
| Peaking | 7247 Hz | 7.57 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Plantronics%20BackBeat%20Fit/Plantronics%20BackBeat%20Fit.png)
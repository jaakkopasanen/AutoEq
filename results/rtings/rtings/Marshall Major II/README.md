# Marshall Major II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.1; 25 -0.0; 28 0.0; 31 0.1; 34 0.2; 37 0.4; 41 0.6; 45 0.8; 49 0.8; 54 0.8; 60 0.7; 66 0.5; 72 0.4; 79 0.3; 87 0.1; 96 0.1; 106 -0.1; 116 -0.2; 128 -0.1; 141 -0.0; 155 0.1; 170 0.3; 187 0.7; 206 1.2; 227 1.8; 249 2.0; 274 1.9; 302 1.3; 332 0.8; 365 0.3; 402 -0.5; 442 -1.4; 486 -1.8; 535 -1.9; 588 -1.7; 647 -1.3; 712 -0.8; 783 -0.4; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.7; 1261 0.6; 1387 0.8; 1526 1.6; 1678 2.2; 1846 2.8; 2031 3.5; 2234 5.2; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.1; 7010 1.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 2.29 | 0.9 dB  |
| Peaking | 266 Hz  | 1.96 | 2.5 dB  |
| Peaking | 534 Hz  | 1.37 | -2.3 dB |
| Peaking | 2898 Hz | 1.16 | 6.2 dB  |
| Peaking | 5316 Hz | 2.42 | 4.8 dB  |
| Peaking | 1343 Hz | 6.12 | -0.4 dB |
| Peaking | 2329 Hz | 8.02 | 1.2 dB  |
| Peaking | 4272 Hz | 2.62 | 2.6 dB  |
| Peaking | 5690 Hz | 1    | -2.8 dB |
| Peaking | 6184 Hz | 5.25 | 4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Marshall%20Major%20II/Marshall%20Major%20II.png)
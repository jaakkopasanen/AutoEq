# Marshall Major II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 0.2; 28 0.2; 31 0.1; 34 0.2; 37 0.2; 41 0.4; 45 0.5; 49 0.5; 54 0.4; 60 0.4; 66 0.3; 72 0.4; 79 0.5; 87 0.5; 96 0.5; 106 0.4; 116 0.4; 128 0.4; 141 0.5; 155 0.7; 170 0.9; 187 1.3; 206 1.7; 227 2.2; 249 2.6; 274 2.6; 302 2.2; 332 1.8; 365 1.3; 402 0.6; 442 -0.2; 486 -0.6; 535 -0.7; 588 -0.6; 647 -0.2; 712 0.0; 783 0.1; 861 -0.0; 947 -0.1; 1042 0.2; 1146 0.9; 1261 0.8; 1387 0.8; 1526 1.2; 1678 1.9; 1846 2.8; 2031 3.9; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 64 Hz   | 0.63 | 0.5 dB  |
| Peaking | 274 Hz  | 1.21 | 4.2 dB  |
| Peaking | 382 Hz  | 0.52 | -1.9 dB |
| Peaking | 2864 Hz | 1.11 | 6.2 dB  |
| Peaking | 5406 Hz | 2.26 | 4.9 dB  |
| Peaking | 1547 Hz | 4.18 | -0.6 dB |
| Peaking | 2272 Hz | 7.79 | 1.0 dB  |
| Peaking | 6475 Hz | 6.3  | 2.4 dB  |
| Peaking | 6677 Hz | 3.03 | 0.4 dB  |
| Peaking | 7717 Hz | 1.98 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Marshall%20Major%20II/Marshall%20Major%20II.png)
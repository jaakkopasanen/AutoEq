# NuForce HEM8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.6; 28 0.5; 31 0.3; 34 0.2; 37 0.0; 41 -0.2; 45 -0.4; 49 -0.6; 54 -0.8; 60 -1.1; 66 -1.5; 72 -1.8; 79 -2.2; 87 -2.6; 96 -3.1; 106 -3.4; 116 -3.6; 128 -4.0; 141 -4.1; 155 -4.3; 170 -4.5; 187 -4.5; 206 -4.5; 227 -4.4; 249 -4.4; 274 -4.2; 302 -4.0; 332 -3.8; 365 -3.5; 402 -3.2; 442 -2.7; 486 -2.4; 535 -2.0; 588 -1.2; 647 -0.6; 712 -0.1; 783 0.4; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -0.1; 1526 1.4; 1678 3.6; 1846 5.7; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.2; 6373 3.9; 7010 2.5; 7711 0.3; 8482 -0.9; 9330 -3.4; 10263 -0.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce HEM8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce HEM8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.2  | 1.1 dB  |
| Peaking | 125 Hz  | 0.63 | -0.5 dB |
| Peaking | 204 Hz  | 0.4  | -4.4 dB |
| Peaking | 3584 Hz | 0.58 | 6.9 dB  |
| Peaking | 9214 Hz | 3.03 | -5.5 dB |
| Peaking | 808 Hz  | 2.19 | 1.6 dB  |
| Peaking | 1378 Hz | 1.69 | -3.8 dB |
| Peaking | 1833 Hz | 2.06 | 4.0 dB  |
| Peaking | 3967 Hz | 0.84 | -1.1 dB |
| Peaking | 5486 Hz | 2.77 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20HEM8/NuForce%20HEM8.png)
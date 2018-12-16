# NuForce EDC3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.4; 28 4.2; 31 4.1; 34 3.9; 37 3.8; 41 3.7; 45 3.5; 49 3.3; 54 3.1; 60 2.8; 66 2.5; 72 2.3; 79 1.9; 87 1.5; 96 1.1; 106 0.7; 116 0.4; 128 0.1; 141 -0.1; 155 -0.3; 170 -0.4; 187 -0.5; 206 -0.6; 227 -1.1; 249 -1.6; 274 -1.8; 302 -1.8; 332 -1.6; 365 -1.4; 402 -1.4; 442 -1.4; 486 -1.3; 535 -1.1; 588 -0.8; 647 -0.6; 712 -0.2; 783 0.1; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.0; 1526 -1.8; 1678 -0.9; 1846 0.2; 2031 1.3; 2234 2.4; 2457 3.3; 2703 4.0; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.3; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.59 | 4.3 dB  |
| Peaking | 58 Hz   | 1.12 | 1.6 dB  |
| Peaking | 312 Hz  | 0.94 | -1.9 dB |
| Peaking | 1470 Hz | 2.63 | -3.2 dB |
| Peaking | 4000 Hz | 0.96 | 6.8 dB  |
| Peaking | 1872 Hz | 3.72 | -0.5 dB |
| Peaking | 3985 Hz | 3.45 | -1.5 dB |
| Peaking | 4047 Hz | 0.83 | 1.1 dB  |
| Peaking | 6310 Hz | 3.64 | 4.5 dB  |
| Peaking | 7320 Hz | 1.36 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/NuForce%20EDC3/NuForce%20EDC3.png)
# NuForce EDC3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.7; 106 4.7; 116 3.8; 128 2.9; 141 2.1; 155 1.4; 170 0.8; 187 0.2; 206 -0.3; 227 -1.2; 249 -1.9; 274 -2.1; 302 -2.0; 332 -1.7; 365 -1.4; 402 -1.4; 442 -1.3; 486 -1.2; 535 -1.0; 588 -0.6; 647 -0.4; 712 -0.1; 783 0.3; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -1.4; 1526 -0.9; 1678 0.1; 1846 1.2; 2031 2.7; 2234 4.3; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -5.7; 16529 -10.8; 18182 -10.1; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.22 | 7.0 dB   |
| Peaking | 252 Hz   | 0.69 | -5.7 dB  |
| Peaking | 1468 Hz  | 1.76 | -4.4 dB  |
| Peaking | 3437 Hz  | 0.57 | 7.1 dB   |
| Peaking | 17578 Hz | 1.36 | -12.4 dB |
| Peaking | 91 Hz    | 5.83 | 0.9 dB   |
| Peaking | 6314 Hz  | 3.08 | 4.2 dB   |
| Peaking | 7419 Hz  | 1.98 | -3.7 dB  |
| Peaking | 13470 Hz | 4.7  | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/NuForce%20EDC3/NuForce%20EDC3.png)
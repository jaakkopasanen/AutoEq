# Turtle Beach Recon 50X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.5; 28 2.1; 31 1.8; 34 1.6; 37 1.5; 41 1.4; 45 1.3; 49 1.3; 54 1.3; 60 1.2; 66 0.9; 72 0.6; 79 0.2; 87 -0.3; 96 -0.6; 106 -0.9; 116 -1.4; 128 -2.1; 141 -2.9; 155 -3.4; 170 -3.8; 187 -3.8; 206 -3.9; 227 -4.2; 249 -4.6; 274 -4.8; 302 -4.5; 332 -4.6; 365 -4.5; 402 -3.6; 442 -3.4; 486 -3.4; 535 -3.4; 588 -3.3; 647 -3.0; 712 -2.5; 783 -1.6; 861 -0.7; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.6; 1387 1.2; 1526 1.8; 1678 2.3; 1846 2.9; 2031 3.4; 2234 3.9; 2457 4.5; 2703 4.2; 2973 3.2; 3270 3.7; 3597 4.6; 3957 4.2; 4353 4.8; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.5; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Recon 50X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Recon 50X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.13 | 2.5 dB  |
| Peaking | 251 Hz  | 0.55 | -5.1 dB |
| Peaking | 625 Hz  | 2.71 | -1.5 dB |
| Peaking | 2464 Hz | 0.91 | 4.0 dB  |
| Peaking | 5276 Hz | 2.29 | 5.6 dB  |
| Peaking | 217 Hz  | 7.02 | 0.5 dB  |
| Peaking | 3079 Hz | 6.34 | -2.0 dB |
| Peaking | 3437 Hz | 2.06 | 1.5 dB  |
| Peaking | 6244 Hz | 4.96 | 2.8 dB  |
| Peaking | 6794 Hz | 1.15 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Turtle%20Beach%20Recon%2050X/Turtle%20Beach%20Recon%2050X.png)
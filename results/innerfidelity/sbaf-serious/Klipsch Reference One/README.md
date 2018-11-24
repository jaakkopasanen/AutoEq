# Klipsch Reference ONE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -4.0; 23 -4.2; 25 -4.4; 28 -4.6; 31 -4.8; 34 -5.0; 37 -5.1; 41 -5.3; 45 -5.5; 49 -5.6; 54 -5.8; 60 -6.1; 66 -6.3; 72 -6.6; 79 -6.8; 87 -7.0; 96 -7.1; 106 -7.0; 116 -7.1; 128 -7.5; 141 -7.6; 155 -7.7; 170 -7.2; 187 -6.9; 206 -6.7; 227 -6.6; 249 -5.9; 274 -4.9; 302 -4.2; 332 -3.8; 365 -3.1; 402 -1.9; 442 -0.5; 486 0.0; 535 1.0; 588 2.2; 647 2.8; 712 2.8; 783 2.4; 861 1.4; 947 0.5; 1042 -0.2; 1146 -0.4; 1261 -0.4; 1387 -1.8; 1526 -2.4; 1678 -2.9; 1846 -3.0; 2031 -3.0; 2234 -3.3; 2457 -3.3; 2703 -3.4; 2973 -2.8; 3270 -1.8; 3597 0.2; 3957 2.8; 4353 4.6; 4788 5.7; 5267 3.3; 5793 2.4; 6373 1.7; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.45 | -5.5 dB |
| Peaking | 141 Hz  | 1.15 | -4.7 dB |
| Peaking | 242 Hz  | 2.05 | -3.6 dB |
| Peaking | 4730 Hz | 4.4  | 6.3 dB  |
| Peaking | 17 Hz   | 1.7  | -0.9 dB |
| Peaking | 357 Hz  | 3.67 | -1.7 dB |
| Peaking | 686 Hz  | 1.66 | 4.0 dB  |
| Peaking | 2763 Hz | 0.79 | -6.9 dB |
| Peaking | 3931 Hz | 0.89 | 5.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)
# Stax SR-003 SA-1993

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.3; 25 4.1; 28 3.8; 31 3.6; 34 3.4; 37 3.3; 41 3.1; 45 2.8; 49 2.6; 54 2.4; 60 2.0; 66 1.7; 72 1.3; 79 0.9; 87 0.4; 96 0.0; 106 -0.4; 116 -0.6; 128 -1.0; 141 -1.3; 155 -1.7; 170 -1.7; 187 -1.9; 206 -2.2; 227 -2.2; 249 -2.4; 274 -2.5; 302 -2.7; 332 -2.7; 365 -2.9; 402 -3.1; 442 -3.2; 486 -3.5; 535 -3.5; 588 -3.0; 647 -2.6; 712 -1.8; 783 -0.7; 861 0.7; 947 0.6; 1042 -0.2; 1146 -1.0; 1261 -2.4; 1387 -3.6; 1526 -5.6; 1678 -5.7; 1846 -3.4; 2031 -1.9; 2234 -0.4; 2457 1.5; 2703 2.4; 2973 4.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.1; 6373 3.1; 7010 0.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.3; 16529 -3.9; 18182 -0.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-003 SA-1993 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-003 SA-1993 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.51 | 4.3 dB  |
| Peaking | 329 Hz   | 0.6  | -3.2 dB |
| Peaking | 1643 Hz  | 2.92 | -6.9 dB |
| Peaking | 3954 Hz  | 1.24 | 7.1 dB  |
| Peaking | 16317 Hz | 2.75 | -4.4 dB |
| Peaking | 567 Hz   | 3    | -1.3 dB |
| Peaking | 896 Hz   | 4.5  | 2.4 dB  |
| Peaking | 5300 Hz  | 6.88 | 1.0 dB  |
| Peaking | 5314 Hz  | 7.42 | 1.1 dB  |
| Peaking | 7808 Hz  | 2.14 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-003%20SA-1993/Stax%20SR-003%20SA-1993.png)
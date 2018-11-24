# Boqari Q1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.5; 66 5.0; 72 4.4; 79 3.8; 87 3.2; 96 2.6; 106 2.1; 116 1.6; 128 1.1; 141 0.5; 155 0.0; 170 -0.4; 187 -0.8; 206 -1.2; 227 -1.5; 249 -2.0; 274 -2.3; 302 -2.6; 332 -2.9; 365 -3.1; 402 -3.3; 442 -3.1; 486 -2.8; 535 -2.6; 588 -2.0; 647 -1.7; 712 -1.3; 783 -0.8; 861 -0.2; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -0.9; 1526 -1.0; 1678 -0.7; 1846 0.0; 2031 1.2; 2234 2.4; 2457 3.9; 2703 5.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.6; 4353 1.8; 4788 -1.9; 5267 -1.5; 5793 3.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Boqari Q1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Boqari Q1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.41 | 6.5 dB  |
| Peaking | 347 Hz  | 0.63 | -3.4 dB |
| Peaking | 3347 Hz | 1.69 | 7.2 dB  |
| Peaking | 4991 Hz | 4.55 | -6.1 dB |
| Peaking | 6215 Hz | 5.34 | 6.1 dB  |
| Peaking | 923 Hz  | 3.63 | 1.1 dB  |
| Peaking | 1598 Hz | 2.62 | -1.6 dB |
| Peaking | 2558 Hz | 5.35 | 1.3 dB  |
| Peaking | 8361 Hz | 4.06 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Boqari%20Q1/Boqari%20Q1.png)
# Beyerdynamic DT X300p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.4; 96 4.3; 106 3.7; 116 2.9; 128 2.4; 141 2.2; 155 1.6; 170 1.5; 187 1.2; 206 1.0; 227 0.9; 249 0.8; 274 1.0; 302 1.0; 332 0.9; 365 0.1; 402 0.0; 442 -0.1; 486 -1.3; 535 -1.3; 588 -1.1; 647 -0.8; 712 -0.6; 783 -0.1; 861 0.0; 947 0.1; 1042 0.1; 1146 0.2; 1261 0.3; 1387 0.3; 1526 1.0; 1678 2.0; 1846 2.4; 2031 3.4; 2234 4.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT X300p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X300p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.32 | 6.0 dB  |
| Peaking | 77 Hz   | 1.96 | 2.2 dB  |
| Peaking | 576 Hz  | 1.83 | -1.6 dB |
| Peaking | 2969 Hz | 1.24 | 6.2 dB  |
| Peaking | 5472 Hz | 2.33 | 4.9 dB  |
| Peaking | 1357 Hz | 3.59 | -0.9 dB |
| Peaking | 2309 Hz | 7.55 | 1.1 dB  |
| Peaking | 6489 Hz | 6.49 | 2.0 dB  |
| Peaking | 6659 Hz | 4.72 | 0.7 dB  |
| Peaking | 7720 Hz | 2.06 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X300p/Beyerdynamic%20DT%20X300p.png)
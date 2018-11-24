# Beyerdynamic DT 48 S 5 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 4.9; 588 3.0; 647 0.8; 712 -0.5; 783 -0.9; 861 -0.6; 947 -0.5; 1042 0.3; 1146 1.1; 1261 1.0; 1387 0.8; 1526 0.6; 1678 -0.2; 1846 -0.9; 2031 -0.3; 2234 1.2; 2457 3.9; 2703 5.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 S 5 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 S 5 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.07 | 6.1 dB  |
| Peaking | 500 Hz  | 1.48 | 3.8 dB  |
| Peaking | 736 Hz  | 1.34 | -6.3 dB |
| Peaking | 1896 Hz | 2.96 | -4.2 dB |
| Peaking | 3790 Hz | 0.86 | 6.8 dB  |
| Peaking | 2226 Hz | 7.13 | -1.2 dB |
| Peaking | 2658 Hz | 3.59 | 1.6 dB  |
| Peaking | 3754 Hz | 2.7  | -1.1 dB |
| Peaking | 6260 Hz | 2.41 | 5.3 dB  |
| Peaking | 7389 Hz | 1.5  | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20S%205%20Ohm/Beyerdynamic%20DT%2048%20S%205%20Ohm.png)
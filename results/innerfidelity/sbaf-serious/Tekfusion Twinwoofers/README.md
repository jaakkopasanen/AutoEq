# Tekfusion Twinwoofers

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.3; 28 -10.5; 31 -10.6; 34 -10.6; 37 -10.6; 41 -10.6; 45 -10.7; 49 -10.8; 54 -10.8; 60 -11.0; 66 -11.1; 72 -11.2; 79 -11.4; 87 -11.5; 96 -11.6; 106 -11.5; 116 -11.4; 128 -11.3; 141 -11.1; 155 -10.8; 170 -10.4; 187 -10.0; 206 -9.4; 227 -8.8; 249 -8.2; 274 -7.3; 302 -6.6; 332 -5.7; 365 -4.8; 402 -3.8; 442 -2.8; 486 -2.0; 535 -1.1; 588 -0.2; 647 -0.0; 712 -0.3; 783 -0.4; 861 1.1; 947 0.3; 1042 -0.1; 1146 -0.2; 1261 -0.1; 1387 -0.0; 1526 0.1; 1678 0.6; 1846 1.5; 2031 2.5; 2234 3.6; 2457 5.1; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.8; 3957 3.6; 4353 0.2; 4788 -2.5; 5267 -4.2; 5793 -2.7; 6373 1.4; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tekfusion Twinwoofers GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tekfusion Twinwoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.26 | -9.9 dB |
| Peaking | 127 Hz  | 0.73 | -6.2 dB |
| Peaking | 251 Hz  | 1.29 | -3.7 dB |
| Peaking | 3160 Hz | 1.34 | 7.0 dB  |
| Peaking | 5061 Hz | 3.85 | -6.9 dB |
| Peaking | 606 Hz  | 3.21 | 1.8 dB  |
| Peaking | 885 Hz  | 4.4  | 1.9 dB  |
| Peaking | 2038 Hz | 0.35 | -1.7 dB |
| Peaking | 2577 Hz | 1.03 | 1.9 dB  |
| Peaking | 6776 Hz | 7.54 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Tekfusion%20Twinwoofers/Tekfusion%20Twinwoofers.png)
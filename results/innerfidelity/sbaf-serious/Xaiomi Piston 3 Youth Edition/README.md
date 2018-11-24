# Xaiomi Piston 3 Youth Edition

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -1.8; 23 -2.1; 25 -2.5; 28 -3.0; 31 -3.5; 34 -4.1; 37 -4.4; 41 -4.6; 45 -5.0; 49 -5.4; 54 -5.6; 60 -5.9; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.3; 96 -7.6; 106 -7.6; 116 -7.7; 128 -7.7; 141 -7.7; 155 -7.7; 170 -7.5; 187 -7.2; 206 -6.9; 227 -6.5; 249 -6.1; 274 -5.6; 302 -5.1; 332 -4.6; 365 -4.0; 402 -3.5; 442 -2.8; 486 -2.4; 535 -1.8; 588 -1.0; 647 -0.5; 712 -0.2; 783 0.3; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.5; 1526 -2.2; 1678 -3.0; 1846 -3.5; 2031 -3.9; 2234 -4.2; 2457 -4.3; 2703 -4.3; 2973 -3.7; 3270 -2.4; 3597 -1.9; 3957 -3.2; 4353 -6.7; 4788 -8.9; 5267 -5.3; 5793 0.2; 6373 3.7; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xaiomi Piston 3 Youth Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xaiomi Piston 3 Youth Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 86 Hz   | 0.44 | -6.5 dB |
| Peaking | 219 Hz  | 0.88 | -3.5 dB |
| Peaking | 2295 Hz | 1.7  | -4.4 dB |
| Peaking | 4799 Hz | 3.8  | -9.6 dB |
| Peaking | 6420 Hz | 4.21 | 5.9 dB  |
| Peaking | 408 Hz  | 2.12 | -0.8 dB |
| Peaking | 819 Hz  | 1.45 | 1.3 dB  |
| Peaking | 1626 Hz | 4.51 | -1.0 dB |
| Peaking | 2914 Hz | 7.47 | -1.0 dB |
| Peaking | 3527 Hz | 7.4  | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xaiomi%20Piston%203%20Youth%20Edition/Xaiomi%20Piston%203%20Youth%20Edition.png)
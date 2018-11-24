# Creative Sound Blaster EVO ZxR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.6; 25 1.7; 28 0.4; 31 -0.6; 34 -1.5; 37 -2.4; 41 -3.4; 45 -4.2; 49 -4.9; 54 -5.5; 60 -6.2; 66 -6.6; 72 -7.0; 79 -7.2; 87 -7.6; 96 -8.0; 106 -8.4; 116 -8.8; 128 -9.2; 141 -9.6; 155 -9.8; 170 -10.0; 187 -10.2; 206 -10.3; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.8; 332 -9.4; 365 -8.6; 402 -7.6; 442 -6.5; 486 -5.3; 535 -3.8; 588 -2.4; 647 -0.7; 712 1.0; 783 1.7; 861 0.9; 947 0.4; 1042 0.1; 1146 0.9; 1261 1.5; 1387 2.6; 1526 3.5; 1678 4.5; 1846 5.7; 2031 6.0; 2234 6.0; 2457 6.0; 2703 5.9; 2973 4.0; 3270 3.4; 3597 4.9; 3957 2.4; 4353 -0.6; 4788 3.1; 5267 3.2; 5793 3.8; 6373 2.7; 7010 1.6; 7711 -2.6; 8482 -6.4; 9330 -6.0; 10263 -1.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound Blaster EVO ZxR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound Blaster EVO ZxR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.69 | 5.1 dB  |
| Peaking | 123 Hz  | 0.41 | -8.4 dB |
| Peaking | 310 Hz  | 1.07 | -5.6 dB |
| Peaking | 2296 Hz | 0.59 | 5.7 dB  |
| Peaking | 8853 Hz | 4.36 | -8.6 dB |
| Peaking | 758 Hz  | 2.56 | 4.7 dB  |
| Peaking | 923 Hz  | 0.94 | -2.7 dB |
| Peaking | 1969 Hz | 2.36 | 1.6 dB  |
| Peaking | 4302 Hz | 9.49 | -4.4 dB |
| Peaking | 5946 Hz | 3.82 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Creative%20Sound%20Blaster%20EVO%20ZxR/Creative%20Sound%20Blaster%20EVO%20ZxR.png)
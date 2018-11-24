# Audeze EL8 Open

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.8; 28 5.7; 31 5.6; 34 5.5; 37 5.5; 41 5.3; 45 5.1; 49 5.0; 54 5.0; 60 4.6; 66 3.8; 72 3.6; 79 3.4; 87 3.2; 96 2.8; 106 2.5; 116 2.4; 128 2.1; 141 1.9; 155 1.6; 170 1.5; 187 1.4; 206 1.2; 227 1.2; 249 1.0; 274 0.9; 302 0.9; 332 1.0; 365 1.2; 402 1.2; 442 1.2; 486 1.1; 535 1.0; 588 1.2; 647 1.1; 712 0.7; 783 0.5; 861 0.3; 947 -0.0; 1042 0.1; 1146 -0.5; 1261 -0.3; 1387 -0.2; 1526 0.1; 1678 0.4; 1846 -0.2; 2031 -1.0; 2234 -1.2; 2457 -0.4; 2703 1.9; 2973 2.4; 3270 2.6; 3597 4.0; 3957 5.0; 4353 3.6; 4788 1.8; 5267 3.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze EL8 Open GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Open ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.41 | 4.9 dB  |
| Peaking | 39 Hz   | 0.06 | 1.0 dB  |
| Peaking | 3810 Hz | 3.24 | 4.7 dB  |
| Peaking | 6117 Hz | 3.7  | 6.7 dB  |
| Peaking | 7666 Hz | 1.64 | -1.0 dB |
| Peaking | 573 Hz  | 2.52 | 0.6 dB  |
| Peaking | 1187 Hz | 4.33 | -0.8 dB |
| Peaking | 2245 Hz | 3.9  | -2.1 dB |
| Peaking | 2795 Hz | 6.43 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Open/Audeze%20EL8%20Open.png)
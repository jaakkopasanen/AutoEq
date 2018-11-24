# Noontec Zoro II Wireless Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -2.1; 23 -2.2; 25 -2.3; 28 -2.5; 31 -2.6; 34 -2.7; 37 -2.7; 41 -2.7; 45 -2.8; 49 -2.8; 54 -2.9; 60 -3.0; 66 -3.1; 72 -3.2; 79 -3.5; 87 -4.0; 96 -4.5; 106 -5.0; 116 -5.3; 128 -5.5; 141 -5.9; 155 -5.9; 170 -5.8; 187 -6.0; 206 -5.9; 227 -5.6; 249 -5.3; 274 -4.8; 302 -4.5; 332 -4.0; 365 -3.6; 402 -3.5; 442 -3.1; 486 -2.8; 535 -2.5; 588 -1.6; 647 -1.1; 712 -0.7; 783 -0.1; 861 -0.1; 947 0.0; 1042 0.0; 1146 0.0; 1261 -0.6; 1387 -1.1; 1526 -1.7; 1678 -1.9; 1846 -1.6; 2031 -0.8; 2234 0.1; 2457 0.8; 2703 1.3; 2973 2.1; 3270 1.7; 3597 2.8; 3957 5.5; 4353 4.1; 4788 1.8; 5267 1.3; 5793 4.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II Wireless Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.51 | -2.2 dB |
| Peaking | 121 Hz  | 1.06 | -2.1 dB |
| Peaking | 224 Hz  | 0.62 | -4.8 dB |
| Peaking | 3981 Hz | 3.84 | 5.3 dB  |
| Peaking | 6247 Hz | 5.44 | 5.9 dB  |
| Peaking | 500 Hz  | 2.47 | -1.0 dB |
| Peaking | 949 Hz  | 0.78 | 1.3 dB  |
| Peaking | 1646 Hz | 2.07 | -2.5 dB |
| Peaking | 2727 Hz | 3.28 | 1.6 dB  |
| Peaking | 3554 Hz | 0.24 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Passive/Noontec%20Zoro%20II%20Wireless%20Passive.png)
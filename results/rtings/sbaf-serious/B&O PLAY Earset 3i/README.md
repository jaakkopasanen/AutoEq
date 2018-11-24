# B&O PLAY Earset 3i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.7; 66 4.7; 72 3.9; 79 3.1; 87 2.3; 96 1.6; 106 1.0; 116 0.5; 128 0.2; 141 -0.0; 155 -0.1; 170 -0.1; 187 -0.2; 206 -0.4; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.4; 365 -0.4; 402 1.2; 442 1.0; 486 1.1; 535 1.0; 588 1.2; 647 1.3; 712 0.8; 783 0.4; 861 0.1; 947 0.0; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.4; 1526 -0.8; 1678 -0.8; 1846 -0.0; 2031 1.4; 2234 3.4; 2457 5.6; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 4.2; 4353 1.7; 4788 1.1; 5267 1.3; 5793 2.3; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O PLAY Earset 3i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O PLAY Earset 3i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.73 | 7.0 dB  |
| Peaking | 578 Hz  | 2.84 | 1.3 dB  |
| Peaking | 1700 Hz | 2.33 | -2.7 dB |
| Peaking | 2916 Hz | 1.52 | 7.0 dB  |
| Peaking | 6444 Hz | 6.96 | 3.8 dB  |
| Peaking | 38 Hz   | 2.61 | -1.5 dB |
| Peaking | 63 Hz   | 1.67 | 1.9 dB  |
| Peaking | 144 Hz  | 0.74 | -1.2 dB |
| Peaking | 3752 Hz | 7.6  | 1.9 dB  |
| Peaking | 4533 Hz | 4.34 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/B&O%20PLAY%20Earset%203i/B&O%20PLAY%20Earset%203i.png)
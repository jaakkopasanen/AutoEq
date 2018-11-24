# Monoprice Enhanced Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.4; 28 1.8; 31 1.4; 34 1.0; 37 0.7; 41 0.3; 45 0.0; 49 -0.2; 54 -0.5; 60 -1.0; 66 -1.4; 72 -1.7; 79 -1.9; 87 -2.2; 96 -2.5; 106 -2.9; 116 -3.2; 128 -3.5; 141 -3.8; 155 -4.0; 170 -4.3; 187 -4.7; 206 -5.1; 227 -5.6; 249 -6.1; 274 -6.6; 302 -7.0; 332 -7.5; 365 -8.0; 402 -8.4; 442 -8.4; 486 -8.4; 535 -7.7; 588 -6.6; 647 -5.0; 712 -3.2; 783 -1.8; 861 -0.8; 947 -0.0; 1042 -0.1; 1146 -0.1; 1261 -0.3; 1387 -0.4; 1526 -0.5; 1678 -0.6; 1846 -0.6; 2031 -0.6; 2234 -0.1; 2457 0.4; 2703 0.0; 2973 -1.4; 3270 -3.4; 3597 -5.8; 3957 -8.3; 4353 -9.4; 4788 -7.2; 5267 -4.1; 5793 -1.1; 6373 -0.5; 7010 -1.1; 7711 -4.2; 8482 -7.1; 9330 -7.2; 10263 -5.9; 11289 -3.8; 12418 -2.8; 13660 -4.8; 15026 -4.1; 16529 -0.2; 18182 0.0; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Enhanced Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Enhanced Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 2.03 | 3.4 dB  |
| Peaking | 338 Hz   | 0.68 | -8.3 dB |
| Peaking | 4226 Hz  | 3.61 | -9.8 dB |
| Peaking | 9679 Hz  | 1.75 | -7.0 dB |
| Peaking | 20459 Hz | 2.33 | -5.8 dB |
| Peaking | 540 Hz   | 1.79 | -5.1 dB |
| Peaking | 640 Hz   | 0.74 | 3.0 dB  |
| Peaking | 943 Hz   | 2.87 | 1.1 dB  |
| Peaking | 11509 Hz | 3.18 | 1.3 dB  |
| Peaking | 14272 Hz | 4.06 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monoprice%20Enhanced%20Active/Monoprice%20Enhanced%20Active.png)
# Corsair HS60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -2.5; 23 -2.7; 25 -3.0; 28 -3.3; 31 -3.6; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.5; 54 -4.6; 60 -4.9; 66 -5.3; 72 -5.6; 79 -6.0; 87 -6.4; 96 -6.8; 106 -7.1; 116 -7.1; 128 -7.1; 141 -7.0; 155 -6.7; 170 -6.1; 187 -5.3; 206 -4.3; 227 -3.2; 249 -2.3; 274 -1.3; 302 -0.5; 332 0.1; 365 0.6; 402 0.8; 442 0.4; 486 -0.3; 535 -1.2; 588 -2.2; 647 -2.6; 712 -2.4; 783 -1.9; 861 -0.8; 947 0.7; 1042 -0.2; 1146 0.2; 1261 0.5; 1387 0.5; 1526 0.7; 1678 0.5; 1846 0.0; 2031 -0.5; 2234 -0.5; 2457 -0.6; 2703 -1.1; 2973 -1.4; 3270 -0.6; 3597 1.6; 3957 1.9; 4353 -2.2; 4788 -4.6; 5267 -2.6; 5793 -1.6; 6373 2.3; 7010 2.5; 7711 -1.5; 8482 -7.5; 9330 -7.6; 10263 -5.0; 11289 -5.6; 12418 -6.7; 13660 -4.9; 15026 -1.8; 16529 -0.4; 18182 -1.5; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.48 | -4.2 dB |
| Peaking | 134 Hz   | 1.17 | -5.5 dB |
| Peaking | 2721 Hz  | 3.26 | -0.7 dB |
| Peaking | 10962 Hz | 1.3  | -6.9 dB |
| Peaking | 20396 Hz | 2.13 | -4.4 dB |
| Peaking | 682 Hz   | 3.11 | -3.3 dB |
| Peaking | 1857 Hz  | 0.12 | 0.7 dB  |
| Peaking | 4849 Hz  | 5.37 | -4.9 dB |
| Peaking | 6792 Hz  | 5.36 | 5.9 dB  |
| Peaking | 8643 Hz  | 6.22 | -5.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS60/Corsair%20HS60.png)
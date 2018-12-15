# AKG K712 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.8; 28 2.3; 31 1.9; 34 1.6; 37 1.3; 41 1.0; 45 0.7; 49 0.5; 54 0.2; 60 -0.1; 66 -0.5; 72 -0.8; 79 -1.2; 87 -1.7; 96 -2.1; 106 -2.5; 116 -3.0; 128 -3.4; 141 -3.8; 155 -4.1; 170 -4.2; 187 -4.3; 206 -4.3; 227 -4.3; 249 -4.4; 274 -4.4; 302 -4.5; 332 -4.5; 365 -4.5; 402 -4.5; 442 -4.5; 486 -4.5; 535 -3.9; 588 -3.8; 647 -3.7; 712 -3.3; 783 -2.5; 861 -1.3; 947 -0.5; 1042 0.1; 1146 -0.2; 1261 -0.6; 1387 -1.2; 1526 -2.1; 1678 -3.7; 1846 -5.7; 2031 -7.1; 2234 -6.9; 2457 -4.6; 2703 -2.2; 2973 -0.3; 3270 -1.3; 3597 -3.3; 3957 -4.5; 4353 -4.5; 4788 -2.9; 5267 -2.2; 5793 -3.2; 6373 -4.7; 7010 -5.4; 7711 -6.5; 8482 -7.3; 9330 -3.3; 10263 0.0; 11289 0.0; 12418 -0.9; 13660 -1.8; 15026 -0.5; 16529 -5.4; 18182 -11.6; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 279 Hz   | 0.5  | -4.9 dB |
| Peaking | 2093 Hz  | 3.05 | -7.2 dB |
| Peaking | 7340 Hz  | 1.6  | -6.2 dB |
| Peaking | 17967 Hz | 2.91 | -8.9 dB |
| Peaking | 19570 Hz | 2.36 | -9.3 dB |
| Peaking | 21 Hz    | 0.98 | 3.6 dB  |
| Peaking | 2958 Hz  | 7.72 | 2.3 dB  |
| Peaking | 4021 Hz  | 4.02 | -3.7 dB |
| Peaking | 8648 Hz  | 4.19 | -7.3 dB |
| Peaking | 9132 Hz  | 1.71 | 5.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K712%20PRO/AKG%20K712%20PRO.png)